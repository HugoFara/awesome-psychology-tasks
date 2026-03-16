#!/usr/bin/env python3
"""Run all audit scripts and produce a combined health report.

Usage:
    python scripts/full_audit.py [--skip-links] [--skip-refs] [--output-dir reports]
"""

import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


def run_script(name: str, args: list[str], label: str) -> tuple[str, int, float]:
    """Run a script, return (output, exit_code, elapsed_seconds)."""
    print(f"  Running {label}...", file=sys.stderr)
    start = time.monotonic()
    result = subprocess.run(
        [sys.executable, str(SCRIPTS / name)] + args,
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    elapsed = time.monotonic() - start
    output = result.stdout
    if result.returncode != 0 and result.stderr:
        output += f"\n\n<!-- stderr: {result.stderr.strip()} -->\n"
    return output, result.returncode, elapsed


def main():
    parser = argparse.ArgumentParser(description="Full audit of the awesome list")
    parser.add_argument("--skip-links", action="store_true", help="Skip link checking (slow)")
    parser.add_argument("--skip-refs", action="store_true", help="Skip reference validation (uses CrossRef API)")
    parser.add_argument("--output-dir", type=str, default=None, help="Save reports to directory")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    sections = []
    any_failure = False

    print(f"Starting full audit at {timestamp}", file=sys.stderr)

    # 1. Implementation audit (always fast, local only)
    output, code, elapsed = run_script("audit_implementations.py", ["--format", "md"], "implementation audit")
    sections.append(("Implementation Audit", output, code, elapsed))
    if code != 0:
        any_failure = True

    # 2. Structure validation
    output, code, elapsed = run_script("validate_structure.py", ["--format", "md"], "structure validation")
    sections.append(("Structure Validation", output, code, elapsed))
    if code != 0:
        any_failure = True

    # 3. Link checking (optional, slow)
    if not args.skip_links:
        output, code, elapsed = run_script("check_links.py", ["--format", "md"], "link check")
        sections.append(("Link Check", output, code, elapsed))
        if code != 0:
            any_failure = True
    else:
        sections.append(("Link Check", "*Skipped (--skip-links)*\n", 0, 0))

    # 4. Reference validation (optional, uses API)
    if not args.skip_refs:
        output, code, elapsed = run_script("validate_references.py", ["--format", "md"], "reference validation")
        sections.append(("Reference Validation", output, code, elapsed))
        if code != 0:
            any_failure = True
    else:
        sections.append(("Reference Validation", "*Skipped (--skip-refs)*\n", 0, 0))

    # Combine into a single report
    lines = [
        f"# Awesome Psychology Tasks — Full Audit Report",
        f"",
        f"Generated: {timestamp}",
        "",
        "## Summary",
        "",
        "| Check | Status | Time |",
        "|-------|--------|------|",
    ]
    for name, _, code, elapsed in sections:
        status = "PASS" if code == 0 else "ISSUES FOUND" if code != 0 else "SKIPPED"
        lines.append(f"| {name} | {status} | {elapsed:.1f}s |")
    lines.append("")
    lines.append("---")
    lines.append("")

    for name, output, _, _ in sections:
        lines.append(f"## {name}")
        lines.append("")
        lines.append(output)
        lines.append("")
        lines.append("---")
        lines.append("")

    report = "\n".join(lines)

    if args.output_dir:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y%m%d")
        out_path = out_dir / f"audit-{date_str}.md"
        out_path.write_text(report)
        print(f"\nReport saved to {out_path}", file=sys.stderr)
    else:
        print(report)

    sys.exit(1 if any_failure else 0)


if __name__ == "__main__":
    main()
