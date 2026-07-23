#!/usr/bin/env python3
"""Build README.md from section fragments + YAML data + vendored JSON.

Inputs (all under this repo — no cross-repo dependency):
    sections/*.md                       — hand-edited prose
    data/platforms.yaml                 — platform tables
    data/collections.yaml               — collection / replication / data tables
    data/source-labels.yaml             — short-label → platform mapping
    data/paradigms.json                 — canonical paradigm list (with domains)
    data/community-implementations.json — known implementations (pipeline output)

Output:
    README.md (overwritten)

Usage:
    python scripts/build_readme.py
    python scripts/build_readme.py --data-dir <dir>   # override JSON source
    python scripts/build_readme.py --check            # exit 1 if README.md is out of date
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
SECTIONS_DIR = ROOT / "sections"
DATA_DIR = ROOT / "data"
# paradigms.json + community-implementations.json are vendored into data/ — the
# pipeline writes community-implementations.json there directly; paradigms.json
# is a snapshot. `--data-dir` overrides this for ad-hoc runs against another source.
DEFAULT_DATA_DIR = DATA_DIR
README = ROOT / "README.md"

# Order of cognitive-domain sections in the README.
DOMAIN_ORDER = [
    "Attention",
    "Memory",
    "Executive Function",
    "Decision Making",
    "Perception",
    "Language",
    "Social Cognition",
    "Learning",
    "Emotion",
    "Creativity",
    "Metacognition",
    "Motor Control",
    "Numerical Cognition",
    "Developmental",
    "Clinical / Screening",
]

STATUS_BADGE = {"active": "🟢", "maintained": "🟡", "legacy": "🔴"}

# Validation state of a paradigm spec — the HUMAN-review axis. Rendered loudly so an
# unreviewed claim is never mistaken for an endorsement (the catalog's north star).
VALIDATION_BADGE = {
    "sourced": "🔵 `sourced` — unreviewed",
    "corroborated": "🟣 `corroborated`",
    "expert-annotated": "🟢 `expert-annotated`",
    "contested": "🟠 `contested`",
}

# verify:task conformance verdict — the MACHINE instrumentation axis (orthogonal to
# validation state). A green verdict is an instrumentation guarantee, not human review.
VERDICT_BADGE = {"conforms": "✅ CONFORMS", "non-conforming": "❌ NON-CONFORMING"}


def _str(v: Any) -> str:
    """Coerce a YAML-loaded scalar to a string, mapping bool → Yes/No.

    YAML 1.1 parses unquoted `Yes`/`No`/`On`/`Off` as booleans, so values
    like `online: Yes` round-trip as Python `True`. Map them back to the
    human label rather than forcing every YAML row to quote.
    """
    if isinstance(v, bool):
        return "Yes" if v else "No"
    return "" if v is None else str(v)


def load_section(name: str) -> str:
    path = SECTIONS_DIR / name
    return path.read_text().rstrip() + "\n"


def load_yaml(name: str) -> Any:
    return yaml.safe_load((DATA_DIR / name).read_text())


def slugify_anchor(heading: str) -> str:
    """GitHub-flavoured Markdown heading-to-anchor conversion.

    GitHub lowercases, strips non-alphanumeric punctuation (so `/` and
    `&` disappear without leaving anything), then replaces *each* space
    with one hyphen — it does NOT collapse runs of whitespace. So
    `Clinical / Screening` → `clinical  screening` → `clinical--screening`.
    """
    s = heading.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = s.replace(" ", "-")
    return s


# ── Tables ──────────────────────────────────────────────────────────────────

def render_platforms_table(rows: list[dict], variant: str) -> str:
    if variant == "open_source" or variant == "commercial":
        header = (
            "| Platform | Description | Language / Tech | Online | Status | Timing | Pricing |\n"
            "|----------|-------------|-----------------|--------|--------|--------|---------|\n"
        )
        lines = []
        for r in rows:
            badge = STATUS_BADGE.get(r["status"], _str(r["status"]))
            lines.append(
                f"| [{_str(r['name'])}]({_str(r['url'])}) | {_str(r['description'])} | "
                f"{_str(r['tech'])} | {_str(r['online'])} | {badge} | "
                f"{_str(r['timing'])} | {_str(r['pricing'])} |"
            )
        return header + "\n".join(lines) + "\n"

    if variant == "survey_clinical":
        header = (
            "| Platform | Description | Online | Pricing |\n"
            "|----------|-------------|--------|---------|\n"
        )
        lines = [
            f"| [{_str(r['name'])}]({_str(r['url'])}) | {_str(r['description'])} | "
            f"{_str(r['online'])} | {_str(r['pricing'])} |"
            for r in rows
        ]
        return header + "\n".join(lines) + "\n"

    if variant == "hosting_backend":
        header = (
            "| Service | Description | Hosts Experiments From |\n"
            "|---------|-------------|------------------------|\n"
        )
        lines = []
        for r in rows:
            desc = _str(r["description"]).strip()
            lines.append(f"| [{_str(r['name'])}]({_str(r['url'])}) | {desc} | {_str(r['hosts'])} |")
        return header + "\n".join(lines) + "\n"

    raise ValueError(f"unknown platforms variant: {variant}")


def load_pipeline_counts() -> dict:
    """Optional sidecar — counts emitted by `pipeline/.../generate-awesome-counts.ts`.

    Returns the empty dict if the file is absent, so a fresh clone can
    still build the README without running the pipeline first.
    """
    path = DATA_DIR / "pipeline-counts.json"
    if not path.exists():
        return {}
    payload = json.loads(path.read_text())
    return payload.get("counts", {})


def load_specs(data_dir: Path) -> dict:
    """Optional vendored paradigm specs — written by the harness's `graduate` step.

    Returns the empty dict if absent, so a fresh clone still builds the README
    without the spec layer.
    """
    path = data_dir / "specs.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def render_specs_section(specs: dict) -> str:
    """Render the paradigm-spec index + audited reference instances.

    Two tables, two axes kept visibly distinct: the spec catalog carries the
    HUMAN-review validation state (loud), and the audited-instances table carries the
    MACHINE verify:task verdict. A green verdict never raises the validation state.
    """
    records = specs.get("specs", [])
    if not records:
        return ""

    out: list[str] = []
    out.append("| Paradigm | Family | Defining contrast | Validation | Executable test |")
    out.append("|----------|--------|-------------------|------------|-----------------|")
    for s in sorted(records, key=lambda r: _str(r["name"]).lower()):
        validation = VALIDATION_BADGE.get(_str(s.get("validationState")), _str(s.get("validationState")))
        executable = "✓ `verify:task`" if s.get("executableSpec") else "—"
        out.append(
            f"| {_str(s['name'])} | {_str(s['family'])} | `{_str(s.get('definingContrast'))}` | "
            f"{validation} | {executable} |"
        )
    table = "\n".join(out) + "\n"

    audited = specs.get("auditedInstances", [])
    if not audited:
        return table

    sub: list[str] = [
        "",
        "### Audited reference instances",
        "",
        "Real third-party implementations driven end-to-end through the executable spec "
        "(`verify:task`). The verdict is a **machine** instrumentation check — it says an "
        "implementation does (or does not) carry the paradigm's defining contrast and scoring; "
        "it is **not** a statement about the spec's human-review state, nor about construct validity.",
        "",
        "| Implementation | Platform | Paradigm | `verify:task` | Notes |",
        "|----------------|----------|----------|---------------|-------|",
    ]
    for a in audited:
        verdict = VERDICT_BADGE.get(_str(a.get("verdict")), _str(a.get("verdict")))
        reason = _str(a.get("reason"))
        if a.get("verdict") == "non-conforming" and reason:
            verdict += f" ({reason})"
        note = _str(a.get("caveat") or a.get("note")).replace("\n", " ").replace("|", "\\|")
        sub.append(
            f"| {_str(a['implementation'])} | {_str(a['platform'])} | {_str(a['spec'])} | {verdict} | {note} |"
        )
    return table + "\n".join(sub) + "\n"


def render_collections_table(rows: list[dict], pipeline_counts: dict) -> str:
    header = (
        "| Collection | Platform | Approx. Tasks | Description |\n"
        "|------------|----------|---------------|-------------|\n"
    )
    lines = []
    for r in rows:
        desc = _str(r["description"]).strip().replace("\n", " ")
        approx = _str(r["approx_tasks"])
        entry = pipeline_counts.get(_str(r["url"]))
        if entry and isinstance(entry.get("count"), int):
            approx = f"{approx} · **{entry['count']:,} indexed**"
        lines.append(
            f"| [{_str(r['name'])}]({_str(r['url'])}) | {_str(r['platform'])} | "
            f"{approx} | {desc} |"
        )
    return header + "\n".join(lines) + "\n"


def render_replication_table(rows: list[dict]) -> str:
    header = (
        "| Project | URL | Description |\n"
        "|---------|-----|-------------|\n"
    )
    lines = [
        f"| [{_str(r['name'])}]({_str(r['url'])}) | {_str(r['location'])} | {_str(r['description'])} |"
        for r in rows
    ]
    return header + "\n".join(lines) + "\n"


def render_data_repos_table(rows: list[dict]) -> str:
    header = (
        "| Repository | URL | Description |\n"
        "|------------|-----|-------------|\n"
    )
    lines = [
        f"| [{_str(r['name'])}]({_str(r['url'])}) | {_str(r['location'])} | {_str(r['description'])} |"
        for r in rows
    ]
    return header + "\n".join(lines) + "\n"


# ── Tasks-by-domain ─────────────────────────────────────────────────────────

def filter_implementations(impls: list[dict], filters: dict, paradigm_slugs: set[str]) -> list[dict]:
    allowed_results = set(filters.get("verification_results", ["passed", "unknown"]))
    require_paradigm = filters.get("require_paradigm", True)
    out = []
    for i in impls:
        result = (i.get("provenance") or {}).get("verificationResult", "unknown") or "unknown"
        if result not in allowed_results:
            continue
        slug = i.get("paradigm")
        if require_paradigm and (slug is None or slug not in paradigm_slugs):
            continue
        out.append(i)
    return out


def freeform_label(impl: dict) -> str:
    """A short label for an implementation that isn't on the curated list.

    The convention in the existing README is to label github-hosted
    implementations by their tech stack (PsychoPy, jsPsych, MATLAB, JS,
    Unity, …). We don't have that field on the impl record yet, so fall
    back to "GitHub" / "OSF" / etc. — close enough for a first cut.
    """
    plat = impl.get("platform")
    return {
        "jspsych": "jsPsych",
        "github": "GitHub",
        "osf": "OSF",
        "otree": "oTree",
    }.get(plat, plat or "Link")


def render_implementations_cell(impls: list[dict], labels_cfg: dict) -> str:
    """Build the `[X](url) · [Y](url)` cell for one paradigm."""
    by_platform: dict[str, list[dict]] = {}
    for i in impls:
        by_platform.setdefault(i.get("platform"), []).append(i)

    label_map = {l["platform"]: l for l in labels_cfg["labels"]}
    freeform_set = set(labels_cfg.get("freeform_platforms", []))

    parts: list[tuple[int, str]] = []  # (priority, rendered)

    for platform, group in by_platform.items():
        if platform in label_map:
            cfg = label_map[platform]
            # README convention is one link per platform: a row with two
            # PsyToolkit Stroop variants would render `[PT] · [PT]` and
            # add noise. Per-label `max_per_paradigm` overrides this.
            cap = cfg.get("max_per_paradigm", 1)
            for impl in group[:cap]:
                parts.append((cfg["priority"], f"[{cfg['short']}]({impl['url']})"))
        elif platform in freeform_set:
            # Free-form (github-hosted) impls don't have a canonical short
            # label, so cap at one per paradigm to avoid `[GitHub] · [GitHub] · …`.
            for impl in group[:1]:
                parts.append((1000, f"[{freeform_label(impl)}]({impl['url']})"))
        # else: silently dropped (e.g. searxng-search) — not curated.

    parts.sort(key=lambda t: (t[0], t[1]))
    return " · ".join(p for _, p in parts)


def render_domain_table(
    domain: str,
    paradigms: list[dict],
    impls_by_paradigm: dict[str, list[dict]],
    labels_cfg: dict,
) -> str:
    rows = sorted(
        [p for p in paradigms if domain in p.get("domains", [])],
        key=lambda p: p["name"].lower(),
    )
    if not rows:
        return ""
    out = [
        f"### {domain}",
        "",
        "| Task | Description | Key Reference | Implementations |",
        "|------|-------------|---------------|-----------------|",
    ]
    for p in rows:
        ref = "; ".join(r.get("citation", "") for r in p.get("keyReferences", []))
        impl_cell = render_implementations_cell(
            impls_by_paradigm.get(p["slug"], []), labels_cfg
        )
        out.append(
            f"| {p['name']} | {p.get('description','')} | {ref} | {impl_cell} |"
        )
    return "\n".join(out) + "\n"


# ── Table of Contents ──────────────────────────────────────────────────────

def build_toc(domain_headings: list[str]) -> str:
    """Auto-generate the Contents block. Mirrors the original README layout."""
    lines = ["## Contents", ""]
    items = [
        ("Choosing a Platform", "choosing-a-platform", []),
        ("Platforms & Frameworks", "platforms--frameworks", [
            ("Open Source", "open-source"),
            ("Commercial / Freemium", "commercial--freemium"),
            ("Survey & Clinical Tools", "survey--clinical-tools"),
            ("Hosting & Backend Services", "hosting--backend-services"),
        ]),
        ("Platform Limitations & Gotchas", "platform-limitations--gotchas", []),
        ("Repositories & Collections", "repositories--collections", []),
        ("Paradigm Specifications", "paradigm-specifications", []),
        ("Tasks by Cognitive Domain", "tasks-by-cognitive-domain",
         [(d, slugify_anchor(d)) for d in domain_headings]),
        ("Contributing", "contributing", []),
        # ("Acknowledgments", "acknowledgments", []),  # held — see build()
        ("License", "license", []),
    ]
    for title, anchor, subs in items:
        lines.append(f"- [{title}](#{anchor})")
        for s_title, s_anchor in subs:
            lines.append(f"  - [{s_title}](#{s_anchor})")
    return "\n".join(lines) + "\n"


# ── Assembly ────────────────────────────────────────────────────────────────

def build(data_dir: Path) -> str:
    paradigms = json.loads((data_dir / "paradigms.json").read_text())
    impls = json.loads((data_dir / "community-implementations.json").read_text())
    platforms = load_yaml("platforms.yaml")
    collections = load_yaml("collections.yaml")
    labels_cfg = load_yaml("source-labels.yaml")
    pipeline_counts = load_pipeline_counts()
    specs = load_specs(data_dir)

    paradigm_slugs = {p["slug"] for p in paradigms}
    impls = filter_implementations(impls, labels_cfg.get("filters", {}), paradigm_slugs)
    impls_by_paradigm: dict[str, list[dict]] = {}
    for i in impls:
        impls_by_paradigm.setdefault(i["paradigm"], []).append(i)

    parts: list[str] = []
    parts.append(load_section("00-header.md"))
    parts.append(build_toc(DOMAIN_ORDER))
    parts.append("---\n")
    parts.append(load_section("10-choosing-a-platform.md"))
    parts.append("---\n")
    parts.append(load_section("20-platforms-intro.md"))
    parts.append("### Open Source\n\n" + render_platforms_table(platforms["open_source"], "open_source"))
    parts.append("### Commercial / Freemium\n\n" + render_platforms_table(platforms["commercial"], "commercial"))
    parts.append("### Survey & Clinical Tools\n\n" + render_platforms_table(platforms["survey_clinical"], "survey_clinical"))
    parts.append("### Hosting & Backend Services\n\n" + render_platforms_table(platforms["hosting_backend"], "hosting_backend"))
    parts.append("---\n")
    parts.append(load_section("30-limitations-and-gotchas.md"))
    parts.append("---\n")
    parts.append(load_section("40-collections-intro.md"))
    parts.append(render_collections_table(collections["collections"], pipeline_counts))
    parts.append("### Collaborative Replication Projects\n\n" + render_replication_table(collections["replication_projects"]))
    parts.append("### Data Repositories\n\n" + render_data_repos_table(collections["data_repositories"]))
    specs_section = render_specs_section(specs)
    if specs_section:
        parts.append("---\n")
        parts.append(load_section("45-paradigm-specs-intro.md"))
        parts.append(specs_section)
    parts.append("---\n")
    parts.append(load_section("50-tasks-by-domain-intro.md"))
    for domain in DOMAIN_ORDER:
        table = render_domain_table(domain, paradigms, impls_by_paradigm, labels_cfg)
        if table:
            parts.append(table)
    parts.append("---\n")
    parts.append(load_section("90-cross-domain.md"))
    parts.append("---\n")
    parts.append(load_section("95-contributing.md"))
    parts.append("---\n")
    # 96-acknowledgments.md is deliberately NOT rendered: the institutional
    # attribution it carries is pending confirmation from the institution. The
    # fragment is kept intact so restoring it is a one-line change here (plus the
    # TOC entry in build_toc) once that confirmation lands.
    parts.append(load_section("97-license.md"))

    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR,
                        help="dir holding paradigms.json + community-implementations.json "
                             "(default: %(default)s)")
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 if README.md differs from generated output")
    parser.add_argument("--output", type=Path, default=README,
                        help="Output path (default: %(default)s)")
    args = parser.parse_args()

    if not args.data_dir.exists():
        print(f"error: data dir not found: {args.data_dir}", file=sys.stderr)
        return 2

    generated = build(args.data_dir)

    if args.check:
        current = args.output.read_text() if args.output.exists() else ""
        if current != generated:
            print(f"{args.output} is out of date — run `python scripts/build_readme.py`",
                  file=sys.stderr)
            return 1
        return 0

    args.output.write_text(generated)
    print(f"wrote {args.output} ({len(generated):,} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
