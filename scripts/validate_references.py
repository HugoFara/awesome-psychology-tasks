#!/usr/bin/env python3
"""Validate references in the awesome list by resolving DOIs and checking metadata.

For each task entry, attempts to:
1. Look up the paper by title/author/year via CrossRef API
2. Verify the DOI resolves
3. Report mismatches in author names, year, or title

Usage:
    python scripts/validate_references.py [--format md|json] [--jobs 5] [--domain Attention]
"""

import argparse
import asyncio
import json
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

try:
    import aiohttp
except ImportError:
    sys.exit("Required: pip install aiohttp")

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

CROSSREF_API = "https://api.crossref.org/works"
HEADERS = {
    "User-Agent": "awesome-psychology-tasks/1.0 (https://github.com/; mailto:contact@example.com)",
    "Accept": "application/json",
}

# Reference patterns: "Author, Year" or "Author & Author, Year" or "Author et al., Year"
REF_RE = re.compile(
    r"^(.+?),\s*(\d{4})$"
)


@dataclass
class Reference:
    domain: str
    task: str
    raw: str
    line: int
    authors_raw: str = ""
    year: str = ""

    # Validation results
    doi: str | None = None
    crossref_title: str | None = None
    crossref_authors: str | None = None
    crossref_year: str | None = None
    match_score: float | None = None
    status: str = "pending"  # pending, found, not_found, error, skipped
    error: str | None = None


def parse_references(text: str) -> list[Reference]:
    """Extract references from task tables."""
    refs = []
    current_domain = None

    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^### (.+)$", line)
        if m:
            current_domain = m.group(1).strip()
            continue

        if current_domain and line.startswith("|") and not line.startswith("|---"):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 3 and cols[0] != "Task":
                task_name = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cols[0]).strip()
                raw_ref = cols[2].strip()

                # Handle multiple references separated by ;
                for single_ref in raw_ref.split(";"):
                    single_ref = single_ref.strip()
                    if not single_ref:
                        continue
                    ref = Reference(
                        domain=current_domain,
                        task=task_name,
                        raw=single_ref,
                        line=i,
                    )
                    m2 = REF_RE.match(single_ref)
                    if m2:
                        ref.authors_raw = m2.group(1).strip()
                        ref.year = m2.group(2).strip()
                    else:
                        ref.status = "skipped"
                        ref.error = "Could not parse author/year"
                    refs.append(ref)
    return refs


async def lookup_crossref(
    session: aiohttp.ClientSession,
    ref: Reference,
    semaphore: asyncio.Semaphore,
) -> Reference:
    if ref.status == "skipped":
        return ref

    query = f"{ref.authors_raw} {ref.year} {ref.task}"
    params = {
        "query": query,
        "rows": 3,
        "select": "DOI,title,author,published-print,published-online,score",
    }

    async with semaphore:
        # Be polite to CrossRef
        await asyncio.sleep(0.2)
        try:
            async with session.get(
                CROSSREF_API,
                params=params,
                timeout=aiohttp.ClientTimeout(total=20),
            ) as resp:
                if resp.status == 429:
                    ref.status = "error"
                    ref.error = "Rate limited by CrossRef"
                    return ref
                if resp.status != 200:
                    ref.status = "error"
                    ref.error = f"HTTP {resp.status}"
                    return ref

                data = await resp.json()
                items = data.get("message", {}).get("items", [])

                if not items:
                    ref.status = "not_found"
                    return ref

                # Take the best match
                best = items[0]
                ref.doi = best.get("DOI", "")
                ref.match_score = best.get("score", 0)

                titles = best.get("title", [])
                ref.crossref_title = titles[0] if titles else None

                authors = best.get("author", [])
                if authors:
                    author_names = []
                    for a in authors[:3]:
                        family = a.get("family", "")
                        given = a.get("given", "")
                        if family:
                            author_names.append(f"{family}, {given}" if given else family)
                    if len(authors) > 3:
                        author_names.append("et al.")
                    ref.crossref_authors = "; ".join(author_names)

                # Extract year from published-print or published-online
                for date_field in ("published-print", "published-online"):
                    date_parts = best.get(date_field, {}).get("date-parts", [[]])
                    if date_parts and date_parts[0]:
                        ref.crossref_year = str(date_parts[0][0])
                        break

                # Check year match
                ref.status = "found"

        except asyncio.TimeoutError:
            ref.status = "error"
            ref.error = "Timeout"
        except Exception as e:
            ref.status = "error"
            ref.error = str(e)[:100]

    return ref


async def run(jobs: int, refs: list[Reference]) -> list[Reference]:
    semaphore = asyncio.Semaphore(jobs)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        tasks = [lookup_crossref(session, ref, semaphore) for ref in refs]
        return await asyncio.gather(*tasks)


def year_matches(ref: Reference) -> bool:
    if not ref.crossref_year or not ref.year:
        return True  # can't check
    return ref.year == ref.crossref_year


def format_markdown(refs: list[Reference]) -> str:
    found = [r for r in refs if r.status == "found"]
    not_found = [r for r in refs if r.status == "not_found"]
    errors = [r for r in refs if r.status == "error"]
    skipped = [r for r in refs if r.status == "skipped"]
    year_mismatches = [r for r in found if not year_matches(r)]

    lines = [
        "# Reference Validation Report",
        "",
        f"**{len(refs)}** references checked · **{len(found)}** found on CrossRef · "
        f"**{len(not_found)}** not found · **{len(year_mismatches)}** year mismatches · "
        f"**{len(errors)}** errors · **{len(skipped)}** skipped",
        "",
    ]

    if not_found:
        lines.append("## References Not Found on CrossRef")
        lines.append("")
        lines.append("These may need manual verification — could be books, unpublished, or pre-DOI era.")
        lines.append("")
        lines.append("| Domain | Task | Reference | Line |")
        lines.append("|--------|------|-----------|------|")
        for r in sorted(not_found, key=lambda x: x.line):
            lines.append(f"| {r.domain} | {r.task} | {r.raw} | {r.line} |")
        lines.append("")

    if year_mismatches:
        lines.append("## Year Mismatches")
        lines.append("")
        lines.append("Listed year differs from CrossRef metadata.")
        lines.append("")
        lines.append("| Domain | Task | Listed | CrossRef Year | DOI |")
        lines.append("|--------|------|--------|---------------|-----|")
        for r in sorted(year_mismatches, key=lambda x: x.line):
            doi_link = f"https://doi.org/{r.doi}" if r.doi else "—"
            lines.append(f"| {r.domain} | {r.task} | {r.raw} | {r.crossref_year} | {doi_link} |")
        lines.append("")

    if found:
        lines.append("## Resolved DOIs")
        lines.append("")
        lines.append("| Domain | Task | Reference | DOI | Score |")
        lines.append("|--------|------|-----------|-----|-------|")
        for r in sorted(found, key=lambda x: (x.domain, x.line)):
            doi_link = f"https://doi.org/{r.doi}" if r.doi else "—"
            score = f"{r.match_score:.1f}" if r.match_score else "—"
            lines.append(f"| {r.domain} | {r.task} | {r.raw} | {doi_link} | {score} |")
        lines.append("")

    if errors:
        lines.append("## Errors")
        lines.append("")
        lines.append("| Domain | Task | Reference | Error |")
        lines.append("|--------|------|-----------|-------|")
        for r in sorted(errors, key=lambda x: x.line):
            lines.append(f"| {r.domain} | {r.task} | {r.raw} | {r.error} |")
        lines.append("")

    return "\n".join(lines)


def format_json(refs: list[Reference]) -> str:
    data = []
    for r in refs:
        entry = {
            "domain": r.domain,
            "task": r.task,
            "reference": r.raw,
            "line": r.line,
            "status": r.status,
        }
        if r.doi:
            entry["doi"] = f"https://doi.org/{r.doi}"
        if r.crossref_title:
            entry["crossref_title"] = r.crossref_title
        if r.crossref_authors:
            entry["crossref_authors"] = r.crossref_authors
        if r.crossref_year:
            entry["crossref_year"] = r.crossref_year
        if r.match_score is not None:
            entry["match_score"] = r.match_score
        if r.error:
            entry["error"] = r.error
        data.append(entry)
    return json.dumps(data, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Validate references via CrossRef")
    parser.add_argument("--format", choices=["md", "json"], default="md")
    parser.add_argument("--jobs", type=int, default=5, help="Max concurrent CrossRef requests")
    parser.add_argument("--domain", type=str, default=None, help="Only check a specific domain")
    args = parser.parse_args()

    text = README.read_text()
    refs = parse_references(text)

    if args.domain:
        refs = [r for r in refs if r.domain.lower() == args.domain.lower()]

    if not refs:
        print("No references found to validate.")
        sys.exit(0)

    print(f"Validating {len(refs)} references via CrossRef...", file=sys.stderr)
    results = asyncio.run(run(args.jobs, refs))

    if args.format == "json":
        print(format_json(results))
    else:
        print(format_markdown(results))

    not_found = sum(1 for r in results if r.status == "not_found")
    year_mismatches = sum(
        1 for r in results if r.status == "found" and not year_matches(r)
    )
    if not_found or year_mismatches:
        sys.exit(1)


if __name__ == "__main__":
    main()
