#!/usr/bin/env python3
"""Validate the non-negotiable ending of an industry report."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADER = (
    "| 公司 | 岗位 | 地域/工作地 | 适用人群 | 来源级别 | 状态与核验日期 | "
    "直接链接 | 匹配判断 | 提醒/独家信息 |"
)


def normalize_table_line(line: str) -> str:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return "| " + " | ".join(cells) + " |"


def validate(text: str) -> list[str]:
    errors: list[str] = []
    lines = text.rstrip().splitlines()
    h2s = [(i, line.strip()) for i, line in enumerate(lines) if re.match(r"^##\s+", line)]

    recruiting = [(i, h) for i, h in h2s if h == "## 实时招聘结果"]
    if len(recruiting) != 1:
        errors.append(f"Expected exactly one '## 实时招聘结果' section; found {len(recruiting)}.")
        return errors

    section_i = recruiting[0][0]
    if h2s[-1][0] != section_i:
        errors.append("'## 实时招聘结果' must be the final H2 section.")

    body = lines[section_i + 1 :]
    nonblank = [(i + section_i + 2, line) for i, line in enumerate(body) if line.strip()]
    if len(nonblank) < 3:
        errors.append("Recruiting section must contain a header, separator, and at least one data row.")
        return errors

    header_no, header = nonblank[0]
    if normalize_table_line(header) != REQUIRED_HEADER:
        errors.append(f"Line {header_no}: recruiting table header does not match the required columns/order.")

    sep_no, sep = nonblank[1]
    if not re.match(r"^\s*\|(?:\s*:?-{3,}:?\s*\|){9}\s*$", sep):
        errors.append(f"Line {sep_no}: expected a 9-column Markdown separator row.")

    for line_no, line in nonblank[2:]:
        if not line.lstrip().startswith("|"):
            errors.append(f"Line {line_no}: content after the recruiting table is not allowed.")
            continue
        if len(line.strip().strip("|").split("|")) != 9:
            errors.append(f"Line {line_no}: expected 9 table cells.")

    earlier = lines[:section_i]
    table_headers = [line for line in earlier if "| 公司 | 岗位 |" in normalize_table_line(line)]
    if table_headers:
        errors.append("Found a recruiting-style job table before the final recruiting section.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    if not args.report.is_file():
        print(f"ERROR: report not found: {args.report}", file=sys.stderr)
        return 2

    errors = validate(args.report.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("OK: recruiting results are one final table at the absolute end of the report.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
