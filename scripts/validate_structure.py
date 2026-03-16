#!/usr/bin/env python3
"""Validate the structural integrity of the awesome list.

Checks:
- Table formatting (consistent columns, no malformed rows)
- Duplicate task entries
- Empty/missing fields
- Alphabetical ordering within tables
- Anchor link validity (TOC → headings)
- Implementation link format consistency

Usage:
    python scripts/validate_structure.py [--format md|json]
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"


@dataclass
class Issue:
    severity: str  # error, warning, info
    category: str
    message: str
    line: int
    context: str = ""


def slugify(text: str) -> str:
    """Convert heading text to GitHub-style anchor.

    GitHub's algorithm: lowercase, strip leading/trailing whitespace,
    replace spaces with -, remove everything except alphanumeric, spaces,
    hyphens, and underscores. Ampersands and slashes get removed.
    """
    text = text.lower().strip()
    # Remove markdown links but keep link text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # GitHub keeps alphanumeric, spaces, hyphens, underscores; removes the rest
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text


def validate(text: str) -> list[Issue]:
    issues: list[Issue] = []
    lines = text.splitlines()

    # Collect all headings for anchor validation
    headings = {}
    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            slug = slugify(m.group(2))
            headings[slug] = i

    # Check TOC anchor links
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"\[([^\]]+)\]\(#([^)]+)\)", line):
            anchor = m.group(2)
            if anchor not in headings:
                issues.append(
                    Issue("error", "anchor", f"Broken TOC link: #{anchor}", i, line.strip())
                )

    # Validate tables
    current_domain = None
    in_table = False
    expected_cols = 0
    task_names: dict[str, list[int]] = {}  # name -> [lines]
    table_tasks: list[tuple[str, int]] = []  # (name, line) for ordering check

    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{2,3})\s+(.+)$", line)
        if m:
            # Check alphabetical ordering of previous table
            if table_tasks and len(table_tasks) > 1:
                sorted_tasks = sorted(table_tasks, key=lambda x: x[0].lower())
                if table_tasks != sorted_tasks:
                    first_out = None
                    for j, (actual, expected) in enumerate(
                        zip(table_tasks, sorted_tasks)
                    ):
                        if actual != expected:
                            first_out = actual
                            break
                    if first_out:
                        issues.append(
                            Issue(
                                "warning",
                                "ordering",
                                f"Table not alphabetically sorted in {current_domain} "
                                f"('{first_out[0]}' at line {first_out[1]} is out of order)",
                                first_out[1],
                            )
                        )

            if m.group(1) == "###":
                current_domain = m.group(2).strip()
            in_table = False
            table_tasks = []
            continue

        # Table header
        if line.startswith("|") and not in_table:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            expected_cols = len(cols)
            in_table = True
            continue

        # Separator
        if in_table and re.match(r"^\|[-\s|:]+\|$", line):
            continue

        # Table row
        if in_table and line.startswith("|"):
            cols = [c.strip() for c in line.split("|")[1:-1]]

            # Column count mismatch
            if len(cols) != expected_cols:
                issues.append(
                    Issue(
                        "error",
                        "table",
                        f"Expected {expected_cols} columns, got {len(cols)}",
                        i,
                        line.strip()[:80],
                    )
                )

            # Empty required fields (first 3 columns in task tables)
            if expected_cols >= 3 and cols[0] != "Task":
                for j, col_name in enumerate(["Task", "Description", "Reference"]):
                    if j < len(cols) and not cols[j].strip():
                        issues.append(
                            Issue("warning", "empty_field", f"Empty {col_name} field", i)
                        )

                # Track task names for duplicate detection
                if cols:
                    name = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cols[0]).strip()
                    if name and name != "Task":
                        task_names.setdefault(name, []).append(i)
                        table_tasks.append((name, i))

            continue

        # End of table
        if in_table and not line.startswith("|"):
            in_table = False

    # Check for duplicates
    for name, line_nums in task_names.items():
        if len(line_nums) > 1:
            issues.append(
                Issue(
                    "warning",
                    "duplicate",
                    f"Duplicate task '{name}' on lines {', '.join(map(str, line_nums))}",
                    line_nums[0],
                )
            )

    # Check for broken markdown links (missing closing parens etc.)
    for i, line in enumerate(lines, 1):
        # Unclosed links
        for m in re.finditer(r"\[[^\]]*$", line):
            issues.append(
                Issue("error", "markdown", "Unclosed markdown link bracket", i, line.strip()[:80])
            )

        # Links with spaces in URL (common error)
        for m in re.finditer(r"\]\(([^)]*\s[^)]*)\)", line):
            url = m.group(1)
            if not url.startswith("#"):  # anchors can have spaces in display text
                issues.append(
                    Issue("warning", "markdown", f"URL contains spaces: {url[:60]}", i)
                )

    return issues


def format_markdown(issues: list[Issue]) -> str:
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]
    infos = [i for i in issues if i.severity == "info"]

    lines = [
        "# Structure Validation Report",
        "",
        f"**{len(errors)}** errors · **{len(warnings)}** warnings · **{len(infos)}** info",
        "",
    ]

    if not issues:
        lines.append("All checks passed.")
        return "\n".join(lines)

    if errors:
        lines.append("## Errors")
        lines.append("")
        lines.append("| Line | Category | Message |")
        lines.append("|------|----------|---------|")
        for i in sorted(errors, key=lambda x: x.line):
            lines.append(f"| {i.line} | {i.category} | {i.message} |")
        lines.append("")

    if warnings:
        lines.append("## Warnings")
        lines.append("")
        lines.append("| Line | Category | Message |")
        lines.append("|------|----------|---------|")
        for i in sorted(warnings, key=lambda x: x.line):
            lines.append(f"| {i.line} | {i.category} | {i.message} |")
        lines.append("")

    return "\n".join(lines)


def format_json(issues: list[Issue]) -> str:
    return json.dumps(
        [
            {
                "severity": i.severity,
                "category": i.category,
                "message": i.message,
                "line": i.line,
                "context": i.context,
            }
            for i in issues
        ],
        indent=2,
    )


def main():
    parser = argparse.ArgumentParser(description="Validate README structure")
    parser.add_argument("--format", choices=["md", "json"], default="md")
    args = parser.parse_args()

    text = README.read_text()
    issues = validate(text)

    if args.format == "json":
        print(format_json(issues))
    else:
        print(format_markdown(issues))

    errors = sum(1 for i in issues if i.severity == "error")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
