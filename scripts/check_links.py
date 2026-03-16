#!/usr/bin/env python3
"""Check all URLs in README.md for availability.

Produces a report of broken, redirected, and slow links.
Uses async HTTP for speed.

Usage:
    python scripts/check_links.py [--timeout 30] [--jobs 10] [--format md|json]
"""

import argparse
import asyncio
import json
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

try:
    import aiohttp
except ImportError:
    sys.exit("Required: pip install aiohttp")

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# Domains to skip — behind auth walls / aggressive bot blocking
SKIP_DOMAINS = {
    "gorilla.sc",
    "app.gorilla.sc",
    "www.millisecond.com",
    "pstnet.com",
    "pavlovia.org",
    "www.healthmeasures.net",
    "opl.apa.org",
    "databrary.org",
    "www.labvanced.com",
    "www.testable.org",
    "osf.io",
}

URL_RE = re.compile(r"https?://[^\s)\]>\"]+")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; awesome-psychology-tasks-linkcheck/1.0)",
    "Accept": "text/html,application/xhtml+xml,*/*",
}


@dataclass
class LinkResult:
    url: str
    line: int
    status: int | None = None
    error: str | None = None
    redirect_url: str | None = None
    elapsed_ms: int = 0
    skipped: bool = False

    @property
    def ok(self) -> bool:
        return self.skipped or (self.status is not None and 200 <= self.status < 400)


def extract_urls(text: str) -> list[tuple[str, int]]:
    """Return (url, line_number) pairs from markdown text."""
    urls = []
    seen = set()
    for i, line in enumerate(text.splitlines(), 1):
        for match in URL_RE.finditer(line):
            url = match.group().rstrip(".,;:!?)")
            if url not in seen:
                seen.add(url)
                urls.append((url, i))
    return urls


def should_skip(url: str) -> bool:
    host = urlparse(url).hostname or ""
    return any(host == d or host.endswith("." + d) for d in SKIP_DOMAINS)


async def check_url(
    session: aiohttp.ClientSession,
    url: str,
    line: int,
    timeout: int,
    semaphore: asyncio.Semaphore,
) -> LinkResult:
    if should_skip(url):
        return LinkResult(url=url, line=line, skipped=True)

    async with semaphore:
        start = time.monotonic()
        try:
            async with session.head(
                url,
                timeout=aiohttp.ClientTimeout(total=timeout),
                allow_redirects=True,
                ssl=False,
            ) as resp:
                elapsed = int((time.monotonic() - start) * 1000)
                redirect = str(resp.url) if str(resp.url) != url else None
                result = LinkResult(
                    url=url,
                    line=line,
                    status=resp.status,
                    redirect_url=redirect,
                    elapsed_ms=elapsed,
                )
                # Retry with GET if HEAD returns 4xx/5xx (some servers reject HEAD)
                if resp.status >= 400:
                    async with session.get(
                        url,
                        timeout=aiohttp.ClientTimeout(total=timeout),
                        allow_redirects=True,
                        ssl=False,
                    ) as resp2:
                        elapsed2 = int((time.monotonic() - start) * 1000)
                        redirect2 = str(resp2.url) if str(resp2.url) != url else None
                        return LinkResult(
                            url=url,
                            line=line,
                            status=resp2.status,
                            redirect_url=redirect2,
                            elapsed_ms=elapsed2,
                        )
                return result
        except asyncio.TimeoutError:
            elapsed = int((time.monotonic() - start) * 1000)
            return LinkResult(url=url, line=line, error="timeout", elapsed_ms=elapsed)
        except Exception as e:
            elapsed = int((time.monotonic() - start) * 1000)
            return LinkResult(
                url=url, line=line, error=str(e)[:120], elapsed_ms=elapsed
            )


async def run(timeout: int, jobs: int) -> list[LinkResult]:
    text = README.read_text()
    urls = extract_urls(text)
    semaphore = asyncio.Semaphore(jobs)

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        tasks = [check_url(session, url, line, timeout, semaphore) for url, line in urls]
        return await asyncio.gather(*tasks)


def format_markdown(results: list[LinkResult]) -> str:
    broken = [r for r in results if not r.ok]
    redirected = [r for r in results if r.ok and r.redirect_url]
    slow = [r for r in results if r.ok and r.elapsed_ms > 5000]
    skipped = [r for r in results if r.skipped]

    lines = ["# Link Check Report", ""]
    total = len(results)
    ok_count = sum(1 for r in results if r.ok and not r.skipped)
    lines.append(
        f"**{total}** links checked · **{ok_count}** OK · "
        f"**{len(broken)}** broken · **{len(redirected)}** redirected · "
        f"**{len(skipped)}** skipped"
    )
    lines.append("")

    if broken:
        lines.append("## Broken Links")
        lines.append("")
        lines.append("| Line | URL | Status | Error |")
        lines.append("|------|-----|--------|-------|")
        for r in sorted(broken, key=lambda x: x.line):
            status = str(r.status) if r.status else "—"
            error = r.error or ""
            lines.append(f"| {r.line} | {r.url} | {status} | {error} |")
        lines.append("")

    if redirected:
        lines.append("## Redirected Links")
        lines.append("")
        lines.append("| Line | Original | Redirects To |")
        lines.append("|------|----------|--------------|")
        for r in sorted(redirected, key=lambda x: x.line):
            lines.append(f"| {r.line} | {r.url} | {r.redirect_url} |")
        lines.append("")

    if slow:
        lines.append("## Slow Links (>5s)")
        lines.append("")
        lines.append("| Line | URL | Time (ms) |")
        lines.append("|------|-----|-----------|")
        for r in sorted(slow, key=lambda x: -x.elapsed_ms):
            lines.append(f"| {r.line} | {r.url} | {r.elapsed_ms} |")
        lines.append("")

    return "\n".join(lines)


def format_json(results: list[LinkResult]) -> str:
    data = []
    for r in results:
        entry = {"url": r.url, "line": r.line, "ok": r.ok}
        if r.status is not None:
            entry["status"] = r.status
        if r.error:
            entry["error"] = r.error
        if r.redirect_url:
            entry["redirect"] = r.redirect_url
        if r.skipped:
            entry["skipped"] = True
        entry["elapsed_ms"] = r.elapsed_ms
        data.append(entry)
    return json.dumps(data, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Check links in README.md")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout per request (seconds)")
    parser.add_argument("--jobs", type=int, default=10, help="Max concurrent requests")
    parser.add_argument("--format", choices=["md", "json"], default="md", help="Output format")
    args = parser.parse_args()

    results = asyncio.run(run(args.timeout, args.jobs))

    if args.format == "json":
        print(format_json(results))
    else:
        print(format_markdown(results))

    broken = [r for r in results if not r.ok]
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
