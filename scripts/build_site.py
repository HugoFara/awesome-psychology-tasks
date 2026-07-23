#!/usr/bin/env python3
"""Build the browsable website from the same data/ the README is built from.

This is the *second renderer* of one corpus. `build_readme.py` renders the corpus
as a Markdown list for people who read GitHub; this renders it as a static site
for people who want to browse, search, and link to a single entry. There is no
second database and no separate content store — if the two ever disagree, one of
them has a bug.

Inputs (all under this repo):
    data/paradigms.json                 — canonical paradigm list
    data/community-implementations.json — pipeline output (metadata only)
    data/specs.json                     — paradigm specs, vendored from the harness
    data/{platforms,collections,source-labels}.yaml
    site/templates/*.html               — page shell and hand-edited prose
    site/static/*                       — CSS and the search script

Output (generated; not committed):
    site/out/ — static HTML, search-index.json, sitemap.xml, robots.txt

Usage:
    python scripts/build_site.py                      # → site/out, GitHub Pages base
    python scripts/build_site.py --base-url / --out /tmp/preview   # local preview
    python scripts/build_site.py --serve              # build, then serve locally
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_readme as readme  # noqa: E402  — shared corpus loaders and domain order

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
TEMPLATES = SITE / "templates"
STATIC = SITE / "static"
DEFAULT_OUT = SITE / "out"
DEFAULT_DATA_DIR = ROOT / "data"

DEFAULT_BASE = "/awesome-psychology-tasks/"
DEFAULT_SITE_URL = "https://hugofara.github.io/awesome-psychology-tasks/"

REPO_URL = "https://github.com/HugoFara/awesome-psychology-tasks"
ISSUE_URL = (
    REPO_URL + "/issues/new?title="
    + quote("Spec review offer: <paradigm>")
    + "&body="
    + quote(
        "Which spec: \nWhich claim(s) I could take "
        "(contrast identification / construct operationalisation / psychometric conditioning): \n"
        "My background: \n\nSend me the attestation dossier for this spec.\n"
    )
)

# The human-review ladder, bottom rung first. Order matters — it is the ladder.
LADDER = [
    ("sourced", "Literature-linked, drafted with LLM assistance or by a contributor, and unreviewed. The honest default."),
    ("corroborated", "Independently cross-checked against the cited sources, but not signed by a named expert."),
    ("expert-annotated", "All three claims attested by named experts. Derived, never self-declared."),
    ("contested", "A named expert disputes at least one claim. A real outcome, kept visible."),
]

# Platforms whose records are indexed but not curated into the README tables. They
# still appear in search, labelled by source, because hiding them would overstate
# how curated the corpus is.
PLATFORM_LABELS = {
    "pavlovia": "Pavlovia",
    "psytoolkit": "PsyToolkit",
    "jspsych-demos": "jsPsych demos",
    "expfactory": "Experiment Factory",
    "childrenhelpingscience": "Children Helping Science",
    "labvanced": "Labvanced",
    "labvanced-samples": "Labvanced samples",
    "test-my-brain": "TestMyBrain",
    "psyflow-web": "psyflow-web",
    "nih-toolbox": "NIH Toolbox",
    "lab-galleries": "Lab gallery",
    "manybabies": "ManyBabies",
    "github": "GitHub",
    "osf": "OSF",
    "otree": "oTree",
    "searxng-search": "Web search (uncurated)",
}


# ── Small helpers ──────────────────────────────────────────────────────────

def esc(value: Any) -> str:
    return html.escape(readme._str(value), quote=True)


def slugify(value: str) -> str:
    s = re.sub(r"[^\w\s-]", "", value.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)


def platform_label(key: str | None) -> str:
    return PLATFORM_LABELS.get(key or "", (key or "Link").replace("-", " ").title())


def doi_link(doi: str | None) -> str:
    if not doi:
        return ""
    return f' <a class="mono small" href="https://doi.org/{esc(doi)}">doi:{esc(doi)}</a>'


def plural(n: int, one: str, many: str | None = None) -> str:
    return one if n == 1 else (many or one + "s")


# ── Corpus ─────────────────────────────────────────────────────────────────

class Corpus:
    """Everything both renderers agree on, loaded once."""

    def __init__(self, data_dir: Path):
        self.paradigms: list[dict] = json.loads((data_dir / "paradigms.json").read_text())
        raw_impls: list[dict] = json.loads((data_dir / "community-implementations.json").read_text())
        self.specs: dict = readme.load_specs(data_dir)
        self.platforms: dict = readme.load_yaml("platforms.yaml")
        self.collections: dict = readme.load_yaml("collections.yaml")
        self.pipeline_counts: dict = readme.load_pipeline_counts()

        self.paradigm_by_slug = {p["slug"]: p for p in self.paradigms}

        # Two filters, both mechanical, both counted openly on the About page.
        # Link health: a record whose last headless check failed is a dead link, not a
        # judgement about the task. Duplicate URLs: the same page reached through two
        # source catalogs is one implementation, and listing it twice would inflate
        # every count on the site.
        self.dead = [
            i for i in raw_impls
            if (i.get("provenance") or {}).get("verificationResult") == "failed"
        ]
        live = [i for i in raw_impls if i not in self.dead]
        seen: set[str] = set()
        self.impls = []
        for impl in live:
            url = (impl.get("url") or "").rstrip("/")
            if url and url in seen:
                continue
            seen.add(url)
            self.impls.append(impl)
        self.duplicates = len(live) - len(self.impls)
        self.total_records = len(raw_impls)

        self.impls_by_paradigm: dict[str, list[dict]] = {}
        for impl in self.impls:
            slug = impl.get("paradigm")
            if slug and slug in self.paradigm_by_slug:
                self.impls_by_paradigm.setdefault(slug, []).append(impl)
        for group in self.impls_by_paradigm.values():
            group.sort(key=lambda i: (platform_label(i.get("platform")), i.get("name", "")))

        self.unmapped = [
            i for i in self.impls
            if not i.get("paradigm") or i["paradigm"] not in self.paradigm_by_slug
        ]
        self.unverified = [
            i for i in self.impls
            if (i.get("provenance") or {}).get("verificationResult") != "passed"
        ]

        # Domains: the README renders a fixed, ordered subset; the site renders every
        # domain present in the data, so no paradigm is invisible here.
        present = {d for p in self.paradigms for d in p.get("domains", [])}
        ordered = [d for d in readme.DOMAIN_ORDER if d in present]
        self.domains = ordered + sorted(present - set(ordered))

        self.spec_records: list[dict] = self.specs.get("specs", [])
        self.audited: list[dict] = self.specs.get("auditedInstances", [])
        self.spec_by_slug = {s["slug"]: s for s in self.spec_records}

    # Counts used in the hero and the footer.
    @property
    def expert_annotated(self) -> int:
        return sum(1 for s in self.spec_records if s.get("validationState") == "expert-annotated")

    @property
    def conforming(self) -> int:
        return sum(1 for a in self.audited if a.get("verdict") == "conforms")

    @property
    def non_conforming(self) -> int:
        return sum(1 for a in self.audited if a.get("verdict") == "non-conforming")

    def paradigms_in(self, domain: str) -> list[dict]:
        return sorted(
            (p for p in self.paradigms if domain in p.get("domains", [])),
            key=lambda p: p["name"].lower(),
        )


# ── Page shell ─────────────────────────────────────────────────────────────

class Renderer:
    def __init__(self, corpus: Corpus, base: str, site_url: str, out: Path):
        self.c = corpus
        self.base = base
        self.site_url = site_url.rstrip("/") + "/"
        self.out = out
        self.shell = (TEMPLATES / "base.html").read_text()
        self.built = date.today().isoformat()
        self.pages: list[str] = []  # paths written, for the sitemap and link check

    def template(self, name: str) -> str:
        return (TEMPLATES / name).read_text()

    def write(
        self,
        path: str,
        *,
        title: str,
        description: str,
        content: str,
        nav: str = "",
        head_extra: str = "",
        body_extra: str = "",
        in_sitemap: bool = True,
    ) -> None:
        counts = (
            f"{len(self.c.paradigms):,} paradigms · {len(self.c.impls):,} implementations · "
            f"{len(self.c.spec_records)} specifications"
        )
        canonical = self.site_url + path.replace("index.html", "")
        page = self.shell
        for key, value in {
            "{{TITLE}}": esc(title),
            "{{DESCRIPTION}}": esc(description),
            "{{CANONICAL}}": esc(canonical),
            "{{BASE}}": self.base,
            "{{CONTENT}}": content,
            "{{HEAD_EXTRA}}": head_extra,
            "{{BODY_EXTRA}}": body_extra,
            "{{FOOT_COUNTS}}": counts,
            "{{BUILT}}": self.built,
        }.items():
            page = page.replace(key, value)
        for slot in ("PARADIGMS", "SPECS", "PLATFORMS", "SEARCH", "REVIEWERS", "ABOUT"):
            page = page.replace(
                "{{NAV_" + slot + "}}", ' aria-current="page"' if nav == slot else ""
            )
        target = self.out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page)
        if in_sitemap:
            self.pages.append(path)

    # ── Shared fragments ───────────────────────────────────────────────────

    def state_badge(self, state: str | None) -> str:
        state = state or "sourced"
        label = {"sourced": "sourced — unreviewed"}.get(state, state)
        return f'<span class="state state--{esc(state)}">{esc(label)}</span>'

    def verdict_badge(self, verdict: str | None, reason: str | None = None) -> str:
        if verdict == "conforms":
            return '<span class="verdict">conforms</span>'
        if verdict == "non-conforming":
            text = "non-conforming"
            if reason:
                text += f" · {reason}"
            return f'<span class="verdict verdict--non-conforming">{esc(text)}</span>'
        return '<span class="verdict verdict--none">not driven</span>'

    def ladder(self, current: str | None = None) -> str:
        rows = []
        reached_index = [s for s, _ in LADDER].index(current) if current in dict(LADDER) else -1
        for index, (state, blurb) in enumerate(LADDER):
            reached = state == "contested" and current == "contested" or (
                index <= reached_index and state != "contested"
            )
            rows.append(
                f'<li data-reached="{str(reached).lower()}" data-current="{str(state == current).lower()}">'
                f"<code>{esc(state)}</code><span>{esc(blurb)}</span></li>"
            )
        return '<ul class="ladder">' + "".join(rows) + "</ul>"

    def impl_table(self, impls: Iterable[dict]) -> str:
        rows = []
        for impl in impls:
            prov = impl.get("provenance") or {}
            checked = prov.get("lastVerifiedAt") or prov.get("fetchedAt") or "—"
            note = "" if prov.get("verificationResult") == "passed" else " · not launch-checked"
            langs = ", ".join(impl.get("languages") or []) or "—"
            rows.append(
                "<tr>"
                f'<td><a href="{esc(impl["url"])}" rel="noopener">{esc(impl.get("name"))}</a></td>'
                f'<td class="mono small">{esc(platform_label(impl.get("platform")))}</td>'
                f'<td class="small">{esc(langs)}</td>'
                f'<td class="mono small num">{esc(checked)}{esc(note)}</td>'
                "</tr>"
            )
        if not rows:
            return '<p class="muted">No implementation indexed for this paradigm yet.</p>'
        return (
            '<div class="scroll-x"><table><thead><tr>'
            "<th>Implementation</th><th>Source</th><th>Languages</th><th>Link checked</th>"
            "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>"
        )

    # ── Pages ──────────────────────────────────────────────────────────────

    def home(self) -> None:
        c = self.c
        specs_n = len(c.spec_records)
        audited_n = len(c.audited)
        wall = f"""
<section class="wall">
  <div class="wall__side">
    <p class="eyebrow">Human review</p>
    <p class="wall__figure wall__figure--human num">{c.expert_annotated}<small> / {specs_n}</small></p>
    <p><strong>specifications reviewed by a named expert.</strong></p>
    <p class="wall__caption">Every specification in the catalog is <code>sourced</code>: drafted, referenced,
    and unreviewed. Raising that state takes a person; no machine check can do it.</p>
    <p><a href="{self.base}reviewers/">Take one spec &rarr;</a></p>
  </div>
  <div class="wall__rule"><span>the wall</span></div>
  <div class="wall__side">
    <p class="eyebrow">Machine checks</p>
    <p class="wall__figure num">{c.conforming}<small> / {audited_n}</small></p>
    <p><strong>audited implementations carry the contrast they claim.</strong></p>
    <p class="wall__caption">Each was driven end-to-end by a responder with a known policy. The
    {c.non_conforming} that failed look like the paradigm and are not wired as it.</p>
    <p><a href="{self.base}specs/">See the verdicts &rarr;</a></p>
  </div>
  <div class="wall__note" style="grid-column:1/-1">
    <strong>The wall is the point.</strong> A machine check confirms a task is wired the way a spec says.
    It cannot tell you the spec is the right way to measure the thing. That judgement is human, so it is
    tracked separately and never inferred from a passing test.
  </div>
</section>"""

        entries = f"""
<section>
  <h2 class="section-head">Start here</h2>
  <div class="grid">
    <article class="card">
      <h3><a href="{self.base}paradigms/">Browse {len(c.paradigms)} paradigms</a></h3>
      <p>Grouped by cognitive domain, each with its description, key references, and every indexed
      implementation.</p>
      <div class="card__foot">{len(c.domains)} domains</div>
    </article>
    <article class="card">
      <h3><a href="{self.base}search/">Search the corpus</a></h3>
      <p>One box across paradigms, specifications, and {len(c.impls):,} implementation records.</p>
      <div class="card__foot">Runs in your browser</div>
    </article>
    <article class="card">
      <h3><a href="{self.base}specs/">Read the specifications</a></h3>
      <p>What it means to implement a paradigm correctly: the defining contrast, the design parameters
      that move results, and an executable test.</p>
      <div class="card__foot">{specs_n} specs · {audited_n} audited instances</div>
    </article>
    <article class="card">
      <h3><a href="{self.base}platforms/">Compare platforms</a></h3>
      <p>Where to build and host: open-source and commercial platforms, timing behaviour, pricing, and
      the large task collections.</p>
      <div class="card__foot">{len(c.platforms.get("open_source", [])) + len(c.platforms.get("commercial", []))} platforms</div>
    </article>
  </div>
</section>"""

        call = f"""
<section class="panel panel--call">
  <p class="eyebrow">Open call</p>
  <h2>The first expert review is the one that matters</h2>
  <p>The catalog's value is not that it lists things &mdash; software can list things. It is that a named
  person, on the record, has judged whether a measurement claim holds. Nobody has done that here yet,
  and the site says so on every page rather than dressing a green check up as review.</p>
  <p>The ask is bounded: <strong>one specification, three separable claims, an afternoon.</strong>
  Sign-offs are named, scoped, dated, and revocable.</p>
  <div class="btn-row">
    <a class="btn btn--primary" href="{self.base}reviewers/">What a review involves</a>
    <a class="btn" href="{ISSUE_URL}">Offer a review</a>
  </div>
</section>"""

        honest = f"""
<section>
  <h2 class="section-head">What this catalog does not claim</h2>
  <div class="grid">
    <article class="card">
      <h3>A link that loads is not a task that works</h3>
      <p>{len(c.impls):,} records survive the headless launch check; {len(c.dead)} failed it and are held
      back. Neither result says anything about the science.</p>
    </article>
    <article class="card">
      <h3>Paradigm labels carry a classifier's error rate</h3>
      <p>{len(c.unmapped):,} records are not confidently mapped to any paradigm and stay out of the
      paradigm pages. Of those that are mapped, the one confirmed error found so far was a mislabel, not
      a broken task.</p>
    </article>
    <article class="card">
      <h3>Specifications are drafts</h3>
      <p>All {specs_n} are unreviewed. They are useful as drafts and dangerous as authority, which is why
      their state is printed next to every one of them.</p>
    </article>
  </div>
  <p style="margin-top:1.25rem"><a href="{self.base}about/">How entries get here, in full &rarr;</a></p>
</section>"""

        self.write(
            "index.html",
            title="Awesome Psychology Tasks — a map of measurement claims",
            description=(
                "A browsable catalog of experimental psychology paradigms and their implementations, "
                "with an honest record of what a human has reviewed and what only a machine has checked."
            ),
            content=self.template("home-intro.html") + wall + call + entries + honest,
        )

    def paradigm_index(self) -> None:
        c = self.c
        jump = "".join(
            f'<li><a href="#{slugify(d)}">{esc(d)} <span class="count">{len(c.paradigms_in(d))}</span></a></li>'
            for d in c.domains
        )
        sections = []
        for domain in c.domains:
            cards = []
            for p in c.paradigms_in(domain):
                impls = c.impls_by_paradigm.get(p["slug"], [])
                spec = c.spec_by_slug.get(p["slug"])
                badge = self.state_badge(spec.get("validationState")) if spec else ""
                cards.append(
                    f'<article class="card"><h3><a href="{self.base}paradigms/{esc(p["slug"])}/">'
                    f'{esc(p["name"])}</a></h3>'
                    f'<p>{esc(p.get("description", ""))}</p>'
                    f'<div class="card__foot"><span>{len(impls)} {plural(len(impls), "implementation")}</span>'
                    f"{badge}</div></article>"
                )
            sections.append(
                f'<section><h2 class="section-head" id="{slugify(domain)}">{esc(domain)} '
                f'<span class="count num">{len(cards)}</span></h2>'
                f'<div class="grid">{"".join(cards)}</div></section>'
            )
        content = f"""
<section>
  <p class="eyebrow">Catalog</p>
  <h1>{len(c.paradigms)} paradigms across {len(c.domains)} domains</h1>
  <p class="lede">Each paradigm carries its description, key references, and every implementation the
  pipeline has indexed and launch-checked. A specification badge means a machine-checkable definition of
  the paradigm exists &mdash; and tells you whether a human has reviewed it.</p>
</section>
<ul class="domain-jump">{jump}</ul>
""" + "".join(sections)
        self.write(
            "paradigms/index.html",
            title="Paradigms — Awesome Psychology Tasks",
            description=f"{len(c.paradigms)} experimental psychology paradigms grouped by cognitive domain, each with references and indexed implementations.",
            content=content,
            nav="PARADIGMS",
        )

    def paradigm_pages(self) -> None:
        c = self.c
        for p in c.paradigms:
            slug = p["slug"]
            impls = c.impls_by_paradigm.get(slug, [])
            spec = c.spec_by_slug.get(slug)
            refs = "".join(
                f'<li>{esc(r.get("citation"))}{doi_link(r.get("doi"))}</li>'
                for r in p.get("keyReferences", [])
            )
            refs_block = (
                f'<section><h2 class="section-head">Key references</h2><ul class="refs">{refs}</ul></section>'
                if refs else ""
            )
            related = "".join(
                f'<li><a class="tag" href="{self.base}paradigms/{esc(r)}/">{esc(c.paradigm_by_slug[r]["name"])}</a></li>'
                for r in p.get("relatedParadigms", [])
                if r in c.paradigm_by_slug
            )
            related_block = (
                f'<section><h2 class="section-head">Related paradigms</h2><ul class="tag-row">{related}</ul></section>'
                if related else ""
            )
            domains = "".join(f'<li><span class="tag">{esc(d)}</span></li>' for d in p.get("domains", []))
            wiki = p.get("wikipediaUrl")
            spec_block = ""
            if spec:
                spec_block = f"""
<section class="panel">
  <p class="eyebrow">Specification</p>
  <h2>{esc(spec["name"])} has a paradigm specification</h2>
  <p>Defining contrast: <code>{esc(spec.get("definingContrast"))}</code></p>
  <p>Human-review state: {self.state_badge(spec.get("validationState"))} &nbsp;
  Executable test: {'<span class="verdict">verify:task</span>' if spec.get("executableSpec") else '<span class="verdict verdict--none">none</span>'}</p>
  <p><a href="{self.base}specs/{esc(spec["slug"])}/">Read the specification &rarr;</a></p>
</section>"""
            content = f"""
<section>
  <p class="eyebrow"><a href="{self.base}paradigms/">Paradigms</a></p>
  <h1>{esc(p["name"])}</h1>
  <p class="lede">{esc(p.get("description", ""))}</p>
  <ul class="tag-row">{domains}</ul>
</section>
{spec_block}
<section>
  <h2 class="section-head">Indexed implementations <span class="count num">{len(impls)}</span></h2>
  <p class="small muted">Metadata only &mdash; each row links to the authors' own page. A date in the last
  column is the last time an automated check confirmed the link loads; it is not a review of the task.</p>
  {self.impl_table(impls)}
</section>
{refs_block}
{related_block}
{'<section><p><a href="' + esc(wiki) + '">Wikipedia article</a></p></section>' if wiki else ''}
"""
            self.write(
                f"paradigms/{slug}/index.html",
                title=f"{p['name']} — Awesome Psychology Tasks",
                description=(p.get("description") or p["name"])[:180],
                content=content,
                nav="PARADIGMS",
            )

    def spec_index(self) -> None:
        c = self.c
        rows = []
        for s in sorted(c.spec_records, key=lambda r: r["name"].lower()):
            rows.append(
                "<tr>"
                f'<td><a href="{self.base}specs/{esc(s["slug"])}/">{esc(s["name"])}</a></td>'
                f'<td class="mono small">{esc(s.get("family"))}</td>'
                f'<td><code class="small">{esc(s.get("definingContrast"))}</code></td>'
                f'<td>{self.state_badge(s.get("validationState"))}</td>'
                f'<td>{"<span class=\"verdict\">verify:task</span>" if s.get("executableSpec") else "<span class=\"verdict verdict--none\">none</span>"}</td>'
                "</tr>"
            )
        audited_rows = []
        for a in c.audited:
            spec = c.spec_by_slug.get(a.get("spec"))
            name = f'<a href="{self.base}specs/{esc(a["spec"])}/">{esc(spec["name"])}</a>' if spec else esc(a.get("spec"))
            audited_rows.append(
                "<tr>"
                f'<td>{esc(a.get("implementation"))}</td>'
                f'<td class="mono small">{esc(a.get("platform"))}</td>'
                f"<td>{name}</td>"
                f'<td>{self.verdict_badge(a.get("verdict"), a.get("reason"))}</td>'
                f'<td class="small">{esc(a.get("note") or a.get("caveat"))}</td>'
                "</tr>"
            )
        content = f"""
<section>
  <p class="eyebrow">Specifications</p>
  <h1>What it means to implement the paradigm correctly</h1>
  <p class="lede">A paradigm specification records the construct a paradigm operationalises, its
  <strong>defining contrast</strong> &mdash; the manipulation and prediction that make it that paradigm
  and not another &mdash; the design parameters that materially move results, and an executable test.</p>
</section>

<section class="wall">
  <div class="wall__side">
    <p class="eyebrow">Human review</p>
    <p>Has a domain expert judged the measurement claims? All {len(c.spec_records)} specifications sit at
    <code>sourced</code>. That is the honest default and already useful. It is not an endorsement.</p>
  </div>
  <div class="wall__rule"><span>the wall</span></div>
  <div class="wall__side">
    <p class="eyebrow">Machine checks</p>
    <p>Does an implementation instantiate the contrast and scoring? A responder with a known policy is
    driven through the real task; the contrast must be logged as a first-class factor, scored, and
    recovered. A pass is drawn in plain ink here, never in green, because it is not review.</p>
  </div>
</section>

<section>
  <h2 class="section-head">The human-review ladder</h2>
  <p>Four states, one axis. A specification climbs it only when a named person signs a claim.</p>
  {self.ladder("sourced")}
</section>

<section>
  <h2 class="section-head">The specifications</h2>
  <div class="scroll-x"><table><thead><tr>
    <th>Paradigm</th><th>Family</th><th>Defining contrast</th><th>Human review</th><th>Executable test</th>
  </tr></thead><tbody>{"".join(rows)}</tbody></table></div>
</section>

<section>
  <h2 class="section-head">Audited reference instances <span class="count num">{len(c.audited)}</span></h2>
  <p class="small muted">Real third-party implementations driven end-to-end through the executable spec.
  The verdict says an implementation does or does not carry the paradigm's defining contrast and scoring.
  It says nothing about the spec's review state, and nothing about construct validity.</p>
  <div class="scroll-x"><table><thead><tr>
    <th>Implementation</th><th>Platform</th><th>Specification</th><th>Verdict</th><th>Note</th>
  </tr></thead><tbody>{"".join(audited_rows)}</tbody></table></div>
</section>

<section class="panel panel--call">
  <h2>None of this is expert-reviewed yet</h2>
  <p>The specs are the part of the catalog a machine cannot finish. Reviewing one is a bounded ask:
  three separable claims, an afternoon, a named and revocable sign-off.</p>
  <div class="btn-row"><a class="btn btn--primary" href="{self.base}reviewers/">Review a specification</a></div>
</section>
"""
        self.write(
            "specs/index.html",
            title="Paradigm specifications — Awesome Psychology Tasks",
            description="Paradigm specifications: defining contrasts, executable tests, and the honest state of human review for each one.",
            content=content,
            nav="SPECS",
        )

    def spec_pages(self) -> None:
        c = self.c
        for s in c.spec_records:
            slug = s["slug"]
            paradigm = c.paradigm_by_slug.get(slug)
            origin = s.get("originReference") or {}
            instances = s.get("referenceInstances", [])
            inst_rows = "".join(
                "<tr>"
                f'<td>{esc(i.get("implementation"))}</td>'
                f'<td class="mono small">{esc(i.get("platform"))}</td>'
                f'<td>{self.verdict_badge(i.get("verdict"), i.get("reason"))}</td>'
                f'<td class="small">{esc(i.get("note"))}</td>'
                "</tr>"
                for i in instances
            )
            inst_block = (
                f"""<section>
  <h2 class="section-head">Implementations driven through this spec</h2>
  <div class="scroll-x"><table><thead><tr>
    <th>Implementation</th><th>Platform</th><th>Verdict</th><th>Note</th>
  </tr></thead><tbody>{inst_rows}</tbody></table></div>
</section>"""
                if inst_rows else ""
            )
            content = f"""
<section>
  <p class="eyebrow"><a href="{self.base}specs/">Specifications</a></p>
  <h1>{esc(s["name"])}</h1>
  <p class="lede">{esc(s.get("abstract"))}</p>
</section>

<section class="panel">
  <dl class="deflist">
    <dt>Defining contrast</dt><dd><code>{esc(s.get("definingContrast"))}</code></dd>
    <dt>Family</dt><dd class="mono">{esc(s.get("family"))}</dd>
    <dt>Human review</dt><dd>{self.state_badge(s.get("validationState"))}</dd>
    <dt>Executable test</dt><dd>{'<span class="verdict">verify:task</span> — an implementation can be driven and judged against this spec' if s.get("executableSpec") else '<span class="verdict verdict--none">none yet</span>'}</dd>
    <dt>Schema</dt><dd class="mono small">spec version {esc(s.get("specVersion"))}</dd>
    {f'<dt>Catalog entry</dt><dd><a href="{self.base}paradigms/{esc(slug)}/">{esc(paradigm["name"])} in the paradigm catalog</a></dd>' if paradigm else ''}
  </dl>
</section>

<section>
  <h2 class="section-head">Where this spec stands</h2>
  <p>This record is <code>{esc(s.get("validationState"))}</code>. The ladder below is the human-review axis
  only &mdash; a passing executable test never moves a record up it.</p>
  {self.ladder(s.get("validationState"))}
</section>

{inst_block}

<section>
  <h2 class="section-head">Origin reference</h2>
  <ul class="refs"><li>{esc(origin.get("citation"))}{doi_link(origin.get("doi"))}</li></ul>
</section>

<section class="panel panel--call">
  <h2>Review this specification</h2>
  <p>Three separable claims: does the contrast identify the paradigm, is it a defensible measure of the
  named construct, and are the psychometric numbers correctly conditioned? Attest one, contest another
  &mdash; a split outcome is a real result.</p>
  <div class="btn-row"><a class="btn btn--primary" href="{self.base}reviewers/">What a review involves</a></div>
</section>
"""
            self.write(
                f"specs/{slug}/index.html",
                title=f"{s['name']} specification — Awesome Psychology Tasks",
                description=(s.get("abstract") or s["name"])[:180],
                content=content,
                nav="SPECS",
            )

    def platforms_page(self) -> None:
        c = self.c

        def table(rows: list[dict], cols: list[tuple[str, str]]) -> str:
            head = "".join(f"<th>{esc(label)}</th>" for label, _ in cols)
            body = []
            for r in rows:
                cells = []
                for _, key in cols:
                    if key == "name":
                        cells.append(f'<td><a href="{esc(r["url"])}">{esc(r["name"])}</a></td>')
                    elif key == "status":
                        cells.append(f'<td class="mono small">{esc(r.get("status"))}</td>')
                    else:
                        cells.append(f'<td class="small">{esc(r.get(key))}</td>')
                body.append("<tr>" + "".join(cells) + "</tr>")
            return (
                f'<div class="scroll-x"><table><thead><tr>{head}</tr></thead>'
                f'<tbody>{"".join(body)}</tbody></table></div>'
            )

        platform_cols = [
            ("Platform", "name"), ("Description", "description"), ("Tech", "tech"),
            ("Online", "online"), ("Status", "status"), ("Timing", "timing"), ("Pricing", "pricing"),
        ]
        collection_rows = []
        for r in c.collections["collections"]:
            indexed = c.pipeline_counts.get(readme._str(r["url"]))
            count = f'{indexed["count"]:,} indexed' if indexed and isinstance(indexed.get("count"), int) else "—"
            collection_rows.append(
                "<tr>"
                f'<td><a href="{esc(r["url"])}">{esc(r["name"])}</a></td>'
                f'<td class="mono small">{esc(r.get("platform"))}</td>'
                f'<td class="mono small num">{esc(r.get("approx_tasks"))}</td>'
                f'<td class="mono small num">{count}</td>'
                f'<td class="small">{esc(readme._str(r.get("description")).strip())}</td>'
                "</tr>"
            )
        content = f"""
<section>
  <p class="eyebrow">Platforms</p>
  <h1>Where to build it, and where to find it</h1>
  <p class="lede">The tooling layer, kept deliberately plain: what each platform is, whether it runs
  online, how it handles timing, and what it costs. Then the large collections this catalog indexes.</p>
</section>

<section>
  <h2 class="section-head">Open source</h2>
  {table(c.platforms["open_source"], platform_cols)}
</section>

<section>
  <h2 class="section-head">Commercial / freemium</h2>
  {table(c.platforms["commercial"], platform_cols)}
</section>

<section>
  <h2 class="section-head">Survey &amp; clinical tools</h2>
  {table(c.platforms["survey_clinical"], [("Platform", "name"), ("Description", "description"), ("Online", "online"), ("Pricing", "pricing")])}
</section>

<section>
  <h2 class="section-head">Hosting &amp; backend services</h2>
  {table(c.platforms["hosting_backend"], [("Service", "name"), ("Description", "description"), ("Hosts experiments from", "hosts")])}
</section>

<section>
  <h2 class="section-head">Collections indexed here</h2>
  <p class="small muted">"Indexed" counts the records this catalog has ingested from that collection, not
  the collection's own total.</p>
  <div class="scroll-x"><table><thead><tr>
    <th>Collection</th><th>Platform</th><th>Approx. tasks</th><th>Indexed here</th><th>Description</th>
  </tr></thead><tbody>{"".join(collection_rows)}</tbody></table></div>
</section>

<section>
  <h2 class="section-head">Replication projects &amp; data repositories</h2>
  {table(c.collections["replication_projects"], [("Project", "name"), ("Where", "location"), ("Description", "description")])}
  <div style="height:1rem"></div>
  {table(c.collections["data_repositories"], [("Repository", "name"), ("Where", "location"), ("Description", "description")])}
</section>
"""
        self.write(
            "platforms/index.html",
            title="Platforms & collections — Awesome Psychology Tasks",
            description="Platforms for building and hosting psychology experiments, plus the task collections this catalog indexes.",
            content=content,
            nav="PLATFORMS",
        )

    def reviewers_page(self) -> None:
        c = self.c
        rows = "".join(
            "<tr>"
            f'<td><a href="{self.base}specs/{esc(s["slug"])}/">{esc(s["name"])}</a></td>'
            f'<td class="mono small">{esc(s.get("family"))}</td>'
            f'<td>{self.state_badge(s.get("validationState"))}</td>'
            "</tr>"
            for s in sorted(c.spec_records, key=lambda r: r["name"].lower())
        )
        table = (
            '<div class="scroll-x"><table><thead><tr><th>Specification</th><th>Family</th>'
            f'<th>Current state</th></tr></thead><tbody>{rows}</tbody></table></div>'
        )
        body = (
            self.template("reviewers-body.html")
            .replace("{{LADDER}}", self.ladder("sourced"))
            .replace("{{SPEC_TABLE}}", table)
            .replace("{{ISSUE_URL}}", ISSUE_URL)
            .replace("{{BASE}}", self.base)
        )
        self.write(
            "reviewers/index.html",
            title="Call for expert reviewers — Awesome Psychology Tasks",
            description="Review one paradigm specification against three separable claims. Named, scoped, revocable sign-offs; an afternoon, not a project.",
            content=body,
            nav="REVIEWERS",
        )

    def about_page(self) -> None:
        c = self.c
        ledger = [
            ("Link checked", "An automated browser opened the URL and it loaded on that date.",
             "Nothing about whether the task runs correctly, or measures anything."),
            ("Paradigm label", "A curated, LLM-assisted assignment of a record to a canonical paradigm.",
             "Not a guarantee: a mislabelled task is the error class this catalog has actually caught."),
            ("Specification", "A drafted, DOI-referenced account of a paradigm's defining contrast.",
             "Not authority. Every spec here is unreviewed by a named expert."),
            ("verify:task conforms", "A responder with a known policy was driven through the real task; "
             "the contrast is logged as a first-class factor, scored, and recovered.",
             "Not validity. The task can be wired exactly as specified and still not measure the construct."),
            ("verify:task non-conforming", "The implementation does not carry the contrast it is "
             "catalogued under — most often it is not logged at all.",
             "Not an accusation of bad science. It can mean the task is fine and the catalog's label is wrong."),
            ("expert-annotated", "Three named claim-level attestations, each scoped and dated.",
             "Never awarded by a passing check, and revocable."),
        ]
        ledger_rows = "".join(
            f"<tr><td class=\"mono small\">{esc(name)}</td><td class=\"small\">{esc(means)}</td>"
            f"<td class=\"small\">{esc(not_means)}</td></tr>"
            for name, means, not_means in ledger
        )
        ledger_table = (
            '<div class="scroll-x"><table><thead><tr><th>Signal</th><th>What it means</th>'
            f'<th>What it does not mean</th></tr></thead><tbody>{ledger_rows}</tbody></table></div>'
        )
        limits = [
            (f"{len(c.dead):,}", "records held back", "their last automated launch check failed"),
            (f"{c.duplicates:,}", "duplicate URLs collapsed", "the same page indexed through more than one source catalog"),
            (f"{len(c.unmapped):,}", "records without a paradigm", "indexed and searchable, but absent from the paradigm pages"),
            (f"{len(c.unverified):,}", "records never launch-checked", "shown, and labelled as such in the tables"),
            (f"{len(c.spec_records) - c.expert_annotated}", "specifications unreviewed", f"of {len(c.spec_records)} — the whole set"),
        ]
        limit_cards = "".join(
            f'<article class="card"><p class="wall__figure num" style="font-size:2rem">{esc(n)}</p>'
            f"<h3>{esc(label)}</h3><p>{esc(note)}</p></article>"
            for n, label, note in limits
        )
        body = (
            self.template("about-body.html")
            .replace("{{LEDGER}}", ledger_table)
            .replace("{{LIMITS}}", f'<div class="grid">{limit_cards}</div>')
            .replace("{{BASE}}", self.base)
        )
        self.write(
            "about/index.html",
            title="About — Awesome Psychology Tasks",
            description="How entries get into the catalog, what each signal does and does not mean, and the known limits of the corpus.",
            content=body,
            nav="ABOUT",
        )

    def search_page(self) -> None:
        c = self.c
        content = f"""
<section>
  <p class="eyebrow">Search</p>
  <h1>One box, {len(c.paradigms) + len(c.spec_records) + len(c.impls):,} records</h1>
  <p class="lede">Paradigms, specifications, and every indexed implementation &mdash; including the
  {len(c.unmapped):,} that are not confidently mapped to a paradigm and so appear nowhere else on the
  site.</p>
</section>
<form class="search-form" id="search-form" role="search">
  <label class="skip" for="q">Search the catalog</label>
  <input class="search-input" id="q" name="q" type="search" placeholder="stroop, working memory, pavlovia…"
         autocomplete="off" disabled>
  <button class="btn" type="submit">Search</button>
</form>
<div class="filters" id="filters" role="group" aria-label="Filter by record type">
  <button type="button" data-kind="all" aria-pressed="true">All</button>
  <button type="button" data-kind="paradigm" aria-pressed="false">Paradigms</button>
  <button type="button" data-kind="spec" aria-pressed="false">Specifications</button>
  <button type="button" data-kind="implementation" aria-pressed="false">Implementations</button>
</div>
<p class="status-line" id="search-status" role="status">Loading the index…</p>
<noscript><p class="noscript-note">Search needs JavaScript. Without it, browse
<a href="{self.base}paradigms/">the paradigm catalog</a> instead.</p></noscript>
<ul class="results" id="results"></ul>
"""
        self.write(
            "search/index.html",
            title="Search — Awesome Psychology Tasks",
            description="Search paradigms, specifications, and implementation records across the catalog.",
            content=content,
            nav="SEARCH",
            body_extra=f'<script src="{self.base}static/search.js" data-base="{self.base}" defer></script>',
        )

    def not_found(self) -> None:
        content = f"""
<section>
  <p class="eyebrow">404</p>
  <h1>That page isn't here</h1>
  <p class="lede">The catalog moves as entries are curated. Try the
  <a href="{self.base}search/">search</a>, or start from the
  <a href="{self.base}paradigms/">paradigm list</a>.</p>
</section>"""
        self.write("404.html", title="Not found — Awesome Psychology Tasks",
                   description="Page not found.", content=content, in_sitemap=False)

    # ── Non-HTML outputs ───────────────────────────────────────────────────

    def search_index(self) -> None:
        c = self.c
        records: list[dict] = []
        for p in c.paradigms:
            records.append({
                "t": p["name"], "u": f"paradigms/{p['slug']}/", "k": "paradigm",
                "s": (p.get("description") or "")[:160],
                "d": ", ".join(p.get("domains", [])), "a": p["slug"],
            })
        for s in c.spec_records:
            records.append({
                "t": f"{s['name']} (specification)", "u": f"specs/{s['slug']}/", "k": "spec",
                "s": (s.get("abstract") or "")[:160], "p": s.get("family"), "a": s["slug"],
            })
        for i in c.impls:
            paradigm = c.paradigm_by_slug.get(i.get("paradigm") or "")
            records.append({
                "t": i.get("name", ""), "u": i.get("url", ""), "k": "implementation",
                "s": (i.get("description") or "")[:160],
                "p": platform_label(i.get("platform")),
                "d": ", ".join(i.get("domains") or []),
                "a": paradigm["name"] if paradigm else "",
            })
        records = [{k: v for k, v in r.items() if v} for r in records]
        path = self.out / "search-index.json"
        path.write_text(json.dumps(records, ensure_ascii=False, separators=(",", ":")))

    def sitemap(self) -> None:
        urls = "".join(
            f"<url><loc>{esc(self.site_url + p.replace('index.html', ''))}</loc>"
            f"<lastmod>{self.built}</lastmod></url>"
            for p in sorted(self.pages)
        )
        (self.out / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>"
        )
        (self.out / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\nSitemap: {self.site_url}sitemap.xml\n"
        )

    def copy_static(self) -> None:
        target = self.out / "static"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(STATIC, target)

    # ── Build + verify ─────────────────────────────────────────────────────

    def build(self) -> None:
        if self.out.exists():
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True)
        self.home()
        self.paradigm_index()
        self.paradigm_pages()
        self.spec_index()
        self.spec_pages()
        self.platforms_page()
        self.reviewers_page()
        self.about_page()
        self.search_page()
        self.not_found()
        self.search_index()
        self.sitemap()
        self.copy_static()

    def check_internal_links(self) -> list[str]:
        """Every in-site href must resolve to a file that was actually written."""
        broken: list[str] = []
        pattern = re.compile(r'href="([^"]+)"')
        for path in self.out.rglob("*.html"):
            for href in pattern.findall(path.read_text()):
                if not href.startswith(self.base) or href.startswith("#"):
                    continue
                rel = href[len(self.base):].split("#")[0].split("?")[0]
                if not rel:
                    continue
                candidate = self.out / rel
                if candidate.is_dir():
                    candidate = candidate / "index.html"
                elif rel.endswith("/"):
                    candidate = self.out / rel / "index.html"
                if not candidate.exists():
                    broken.append(f"{path.relative_to(self.out)} → {href}")
        return sorted(set(broken))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--base-url", default=DEFAULT_BASE,
                        help="path the site is served from (default: %(default)s; use / for local preview)")
    parser.add_argument("--site-url", default=DEFAULT_SITE_URL,
                        help="absolute site URL, for canonical links and the sitemap")
    parser.add_argument("--serve", action="store_true", help="serve the built site on :8000 afterwards")
    args = parser.parse_args()

    if not args.data_dir.exists():
        print(f"error: data dir not found: {args.data_dir}", file=sys.stderr)
        return 2

    base = args.base_url if args.base_url.endswith("/") else args.base_url + "/"
    corpus = Corpus(args.data_dir)
    renderer = Renderer(corpus, base, args.site_url, args.out)
    renderer.build()

    broken = renderer.check_internal_links()
    if broken:
        print("error: broken internal links:", file=sys.stderr)
        for item in broken[:20]:
            print("  " + item, file=sys.stderr)
        return 1

    total = sum(1 for _ in args.out.rglob("*.html"))
    index_size = (args.out / "search-index.json").stat().st_size
    print(f"wrote {total:,} pages to {args.out} (search index {index_size / 1024:,.0f} KB)")

    if args.serve:
        import functools
        import http.server
        import socketserver

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(args.out))
        with socketserver.TCPServer(("", 8000), handler) as httpd:
            print(f"serving {args.out} at http://localhost:8000{base}  (ctrl-c to stop)")
            httpd.serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
