#!/usr/bin/env python3
"""Audit the awesome list for tasks missing implementations.

Parses the task tables in README.md, identifies which tasks have zero
implementation links, and produces a prioritized report for filling gaps.

Usage:
    python scripts/audit_implementations.py [--format md|json|csv]
"""

import argparse
import csv
import io
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# Known implementation link abbreviations
IMPL_ABBREVS = ["PT", "Ms", "EF", "Go", "Pv", "jP", "TB", "NIH Toolbox", "Niv Lab"]


@dataclass
class Task:
    domain: str
    name: str
    description: str
    reference: str
    implementations_raw: str
    line: int

    @property
    def implementation_count(self) -> int:
        if not self.implementations_raw.strip():
            return 0
        # Count markdown links
        return len(re.findall(r"\[", self.implementations_raw))

    @property
    def implementation_platforms(self) -> list[str]:
        return re.findall(r"\[([^\]]+)\]", self.implementations_raw)

    @property
    def has_implementations(self) -> bool:
        return self.implementation_count > 0


def parse_tasks(text: str) -> list[Task]:
    """Parse all task tables from the README."""
    tasks = []
    current_domain = None
    in_table = False
    header_seen = False

    for i, line in enumerate(text.splitlines(), 1):
        # Detect domain headers (### level)
        m = re.match(r"^### (.+)$", line)
        if m:
            current_domain = m.group(1).strip()
            in_table = False
            header_seen = False
            continue

        if current_domain is None:
            continue

        # Detect task tables by header row
        if re.match(r"\|\s*Task\s*\|.*Description.*\|.*Reference.*\|.*Implementations?\s*\|", line):
            in_table = True
            header_seen = False
            continue

        # Skip separator row
        if in_table and re.match(r"\|[-\s|]+\|$", line):
            header_seen = True
            continue

        # Parse task rows
        if in_table and header_seen and line.startswith("|"):
            cols = [c.strip() for c in line.split("|")]
            # Split produces empty strings at start/end
            cols = [c for c in cols if c != "" or cols.index(c) not in (0, len(cols) - 1)]
            cols = line.split("|")[1:-1]  # more reliable
            cols = [c.strip() for c in cols]

            if len(cols) >= 4:
                tasks.append(
                    Task(
                        domain=current_domain,
                        name=re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cols[0]).strip(),
                        description=cols[1].strip(),
                        reference=cols[2].strip(),
                        implementations_raw=cols[3].strip() if len(cols) > 3 else "",
                        line=i,
                    )
                )
            continue

        # End of table
        if in_table and header_seen and not line.startswith("|"):
            in_table = False

    return tasks


def format_markdown(tasks: list[Task]) -> str:
    total = len(tasks)
    with_impl = sum(1 for t in tasks if t.has_implementations)
    without = total - with_impl

    lines = [
        "# Implementation Audit Report",
        "",
        f"**{total}** tasks total · **{with_impl}** with implementations ({with_impl*100//total}%) "
        f"· **{without}** missing implementations",
        "",
    ]

    # Group missing by domain
    missing_by_domain: dict[str, list[Task]] = {}
    for t in tasks:
        if not t.has_implementations:
            missing_by_domain.setdefault(t.domain, []).append(t)

    lines.append("## Tasks Missing Implementations")
    lines.append("")

    for domain, domain_tasks in missing_by_domain.items():
        domain_total = sum(1 for t in tasks if t.domain == domain)
        domain_with = domain_total - len(domain_tasks)
        pct = domain_with * 100 // domain_total if domain_total else 0
        lines.append(f"### {domain} ({domain_with}/{domain_total} = {pct}% covered)")
        lines.append("")
        lines.append("| Task | Reference | Line |")
        lines.append("|------|-----------|------|")
        for t in domain_tasks:
            lines.append(f"| {t.name} | {t.reference} | {t.line} |")
        lines.append("")

    # Coverage summary table
    lines.append("## Coverage by Domain")
    lines.append("")
    lines.append("| Domain | Total | With Impl | Missing | Coverage |")
    lines.append("|--------|-------|-----------|---------|----------|")

    domains_seen = []
    for t in tasks:
        if t.domain not in [d[0] for d in domains_seen]:
            domains_seen.append((t.domain, []))
        for d in domains_seen:
            if d[0] == t.domain:
                d[1].append(t)

    for domain, domain_tasks in domains_seen:
        dt = len(domain_tasks)
        dw = sum(1 for t in domain_tasks if t.has_implementations)
        dm = dt - dw
        pct = dw * 100 // dt if dt else 0
        bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
        lines.append(f"| {domain} | {dt} | {dw} | {dm} | {bar} {pct}% |")
    lines.append("")

    # Platform coverage
    lines.append("## Platform Coverage")
    lines.append("")
    platform_counts: dict[str, int] = {}
    for t in tasks:
        for p in t.implementation_platforms:
            platform_counts[p] = platform_counts.get(p, 0) + 1

    lines.append("| Platform | Tasks Covered |")
    lines.append("|----------|---------------|")
    for p, c in sorted(platform_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {p} | {c} |")
    lines.append("")

    return "\n".join(lines)


def format_json(tasks: list[Task]) -> str:
    data = []
    for t in tasks:
        data.append(
            {
                "domain": t.domain,
                "name": t.name,
                "reference": t.reference,
                "line": t.line,
                "implementation_count": t.implementation_count,
                "platforms": t.implementation_platforms,
                "has_implementations": t.has_implementations,
            }
        )
    return json.dumps(data, indent=2)


def format_csv(tasks: list[Task]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["domain", "task", "reference", "line", "impl_count", "platforms", "has_impl"])
    for t in tasks:
        writer.writerow(
            [
                t.domain,
                t.name,
                t.reference,
                t.line,
                t.implementation_count,
                "; ".join(t.implementation_platforms),
                t.has_implementations,
            ]
        )
    return buf.getvalue()


def main():
    parser = argparse.ArgumentParser(description="Audit task implementations")
    parser.add_argument("--format", choices=["md", "json", "csv"], default="md")
    parser.add_argument("--missing-only", action="store_true", help="Only show tasks without implementations")
    args = parser.parse_args()

    text = README.read_text()
    tasks = parse_tasks(text)

    if args.missing_only:
        tasks_to_report = [t for t in tasks if not t.has_implementations]
    else:
        tasks_to_report = tasks

    if args.format == "json":
        print(format_json(tasks_to_report))
    elif args.format == "csv":
        print(format_csv(tasks_to_report))
    else:
        print(format_markdown(tasks))

    missing = sum(1 for t in tasks if not t.has_implementations)
    if missing:
        print(f"\n<!-- {missing} tasks need implementations -->", file=sys.stderr)


if __name__ == "__main__":
    main()
