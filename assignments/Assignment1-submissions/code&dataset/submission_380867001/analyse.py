#!/usr/bin/env python3
"""
analyse.py - Consolidate and analyze T3 Benchmark cases

Consolidates [author]_cases.json files from subdirectories into a single
BenchmarkT3_Extension_B.json file and generates summary statistics.

Author: Generated with Claude Code
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from typing import Any


# =============================================================================
# Configuration
# =============================================================================

TARGET_TOTAL = 460  # Target total cases for Economics (Bucket B)

# Target distributions (percentages) from CLAUDE.md
PEARL_TARGETS = {
    "L1": 11,   # 11% = 51 cases
    "L2": 67,   # 67% = 308 cases
    "L3": 22,   # 22% = 101 cases
}

DIFFICULTY_TARGETS = {
    "Easy": 15,    # 15% = 69 cases
    "Medium": 59,  # 59% = 271 cases
    "Hard": 26,    # 26% = 120 cases
}

TRAP_TARGETS = {
    "CONF-MED": 36,        # 36% = 166 cases
    "COUNTERFACTUAL": 22,  # 22% = 101 cases
    "REVERSE": 13,         # 13% = 60 cases
    "SELECTION": 11,       # 11% = 51 cases
    "COLLIDER": 7,         # 7% = 32 cases
    "MECHANISM": 2,        # 2% = 9 cases
}

# L3 Ground Truth targets (as % of L3 cases)
L3_GROUND_TRUTH_TARGETS = {
    "VALID": 30,       # 30% of L3 cases
    "INVALID": 10,     # 10% of L3 cases
    "CONDITIONAL": 60, # 60% of L3 cases
}


# =============================================================================
# Mandatory Field Definitions by Pearl Level
# =============================================================================

BASE_MANDATORY = [
    "id",
    "bucket",
    "case_id",
    "pearl_level",
    "pearl_level_name",
    "domain_id",
    "domain_name",
    "scenario",
    "claim",
    "label",
    "label_name",
    "trap",
    "trap.type",
    "variables",
    "variables.X",
    "variables.Y",
    "hidden_structure",
    "hidden_structure.dag_edges",
    "gold_rationale",
    "difficulty",
    "annotation",
    "annotation.wise_refusal",
]

L2_MANDATORY = [
    # answer_if_tz_lt_tx and answer_if_tx_lt_tz are optional
]

L3_MANDATORY = [
    "hidden_structure.counterfactual_query",
    "hidden_structure.ground_truth",
    "variables.Y0",
]


def get_nested_value(obj: dict, path: str) -> Any:
    """Get a nested value from a dict using dot notation."""
    keys = path.split(".")
    current = obj
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
        if current is None:
            return None
    return current


def check_mandatory_fields(case: dict) -> list[str]:
    """Check a case for missing mandatory fields. Returns list of missing fields."""
    missing = []
    pearl_level = case.get("pearl_level", "")

    # Check base mandatory fields
    for field in BASE_MANDATORY:
        value = get_nested_value(case, field)
        if value is None or value == "" or value == []:
            missing.append(field)

    # Check L2-specific fields
    if pearl_level == "L2":
        for field in L2_MANDATORY:
            value = get_nested_value(case, field)
            if value is None or value == "":
                missing.append(field)

    # Check L3-specific fields
    if pearl_level == "L3":
        for field in L3_MANDATORY:
            value = get_nested_value(case, field)
            if value is None or value == "":
                missing.append(field)

    return missing


def load_cases_from_author(author_dir: Path) -> tuple[str, list[dict]]:
    """Load cases from an author's directory."""
    author = author_dir.name
    cases = []

    # Look for [author]_cases.json
    json_file = author_dir / f"{author}_cases.json"
    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as f:
            cases = json.load(f)
        print(f"  {author}: Loaded {len(cases)} cases from {json_file.name}")
    else:
        print(f"  {author}: No {author}_cases.json found")

    return author, cases


def make_table_with_targets(data: dict[str, dict[str, int]],
                            targets: dict[str, int],
                            row_order: list[str] = None,
                            col_order: list[str] = None,
                            title: str = "",
                            total_cases: int = 0) -> str:
    """Generate a formatted markdown table with targets and percentages."""
    if not data:
        return f"### {title}\n\n*No data*\n"

    # Get all columns (authors) and rows
    all_cols = set()
    all_rows = set()
    for row, cols in data.items():
        all_rows.add(row)
        all_cols.update(cols.keys())

    # Apply ordering
    if col_order:
        cols = [c for c in col_order if c in all_cols]
        cols.extend(sorted(all_cols - set(cols)))
    else:
        cols = sorted(all_cols)

    if row_order:
        rows = [r for r in row_order if r in all_rows]
        rows.extend(sorted(all_rows - set(rows)))
    else:
        rows = sorted(all_rows)

    # Build table
    lines = []
    if title:
        lines.append(f"### {title}")
        lines.append("")

    # Header row - add Target columns
    header = f"| Category |"
    for col in cols:
        header += f" {col} |"
    header += " Total | % | Target | Target % |"
    lines.append(header)

    # Separator
    sep = "| :--- |"
    for _ in cols:
        sep += " ---: |"
    sep += " ---: | ---: | ---: | ---: |"
    lines.append(sep)

    # Data rows
    col_totals = {col: 0 for col in cols}
    grand_total = 0

    for row in rows:
        row_data = data.get(row, {})
        row_total = sum(row_data.values())
        grand_total += row_total

        # Calculate percentage of current total
        pct = (row_total / total_cases * 100) if total_cases > 0 else 0

        # Get target for this row
        target_pct = targets.get(row, 0)
        target_count = int(TARGET_TOTAL * target_pct / 100)

        line = f"| {row} |"
        for col in cols:
            val = row_data.get(col, 0)
            col_totals[col] += val
            line += f" {val} |"
        line += f" {row_total} | {pct:.1f}% | {target_count} | {target_pct}% |"
        lines.append(line)

    # Totals row with percentages
    total_pct = (grand_total / total_cases * 100) if total_cases > 0 else 0
    target_pct_sum = sum(targets.values())

    total_line = f"| **Total** |"
    for col in cols:
        total_line += f" **{col_totals[col]}** |"
    total_line += f" **{grand_total}** | **{total_pct:.1f}%** | **{TARGET_TOTAL}** | **{target_pct_sum}%** |"
    lines.append(total_line)

    lines.append("")
    return "\n".join(lines)


def make_l3_ground_truth_table(data: dict[str, dict[str, int]],
                                col_order: list[str] = None,
                                total_l3_cases: int = 0) -> str:
    """Generate a table for L3 ground truth distribution."""
    if not data:
        return "### L3 Ground Truth Distribution\n\n*No L3 cases found*\n"

    # Get all columns (authors) and rows
    all_cols = set()
    all_rows = set()
    for row, cols in data.items():
        all_rows.add(row)
        all_cols.update(cols.keys())

    # Apply ordering
    if col_order:
        cols = [c for c in col_order if c in all_cols]
        cols.extend(sorted(all_cols - set(cols)))
    else:
        cols = sorted(all_cols)

    rows = ["VALID", "INVALID", "CONDITIONAL"]
    rows.extend(sorted(all_rows - set(rows)))

    # Calculate target L3 count (22% of 460)
    target_l3_total = int(TARGET_TOTAL * PEARL_TARGETS.get("L3", 22) / 100)

    # Build table
    lines = []
    lines.append("### L3 Ground Truth Distribution")
    lines.append("")

    # Header row
    header = "| Ground Truth |"
    for col in cols:
        header += f" {col} |"
    header += " Total | % | Target | Target % |"
    lines.append(header)

    # Separator
    sep = "| :--- |"
    for _ in cols:
        sep += " ---: |"
    sep += " ---: | ---: | ---: | ---: |"
    lines.append(sep)

    # Data rows
    col_totals = {col: 0 for col in cols}
    grand_total = 0

    for row in rows:
        row_data = data.get(row, {})
        row_total = sum(row_data.values())
        grand_total += row_total

        # Calculate percentage of L3 total
        pct = (row_total / total_l3_cases * 100) if total_l3_cases > 0 else 0

        # Get target for this row (as % of L3 cases)
        target_pct = L3_GROUND_TRUTH_TARGETS.get(row, 0)
        target_count = int(target_l3_total * target_pct / 100)

        line = f"| {row} |"
        for col in cols:
            val = row_data.get(col, 0)
            col_totals[col] += val
            line += f" {val} |"
        line += f" {row_total} | {pct:.1f}% | {target_count} | {target_pct}% |"
        lines.append(line)

    # Totals row
    total_pct = (grand_total / total_l3_cases * 100) if total_l3_cases > 0 else 0

    total_line = "| **Total** |"
    for col in cols:
        total_line += f" **{col_totals[col]}** |"
    total_line += f" **{grand_total}** | **{total_pct:.1f}%** | **{target_l3_total}** | **100%** |"
    lines.append(total_line)

    lines.append("")
    return "\n".join(lines)


def make_flags_table(flags: list[dict]) -> str:
    """Generate a flags table for cases with missing fields."""
    if not flags:
        return "### Flags\n\n*No missing mandatory fields detected.*\n"

    lines = []
    lines.append("### Flags")
    lines.append("")
    lines.append("Cases with missing mandatory fields:")
    lines.append("")
    lines.append("| Author | Case ID | Pearl | Missing Fields |")
    lines.append("| ------ | ------: | :---: | -------------- |")

    for flag in sorted(flags, key=lambda x: (x["author"], x["case_id"])):
        missing_str = ", ".join(flag["missing"][:5])
        if len(flag["missing"]) > 5:
            missing_str += f" (+{len(flag['missing']) - 5} more)"
        lines.append(f"| {flag['author']} | {flag['case_id']} | {flag['pearl_level']} | {missing_str} |")

    lines.append("")
    lines.append(f"**Total flagged cases: {len(flags)}**")
    lines.append("")
    return "\n".join(lines)


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent

    print("=" * 60)
    print("T3 Benchmark Case Analysis")
    print("=" * 60)
    print()

    # Find all author subdirectories (exclude hidden dirs and __pycache__)
    author_dirs = [d for d in script_dir.iterdir()
                   if d.is_dir() and not d.name.startswith('.') and d.name != '__pycache__']

    print(f"Found {len(author_dirs)} author directories: {', '.join(d.name for d in author_dirs)}")
    print()
    print("Loading cases:")

    # Load cases from each author
    all_cases = []
    cases_by_author = {}

    for author_dir in sorted(author_dirs):
        author, cases = load_cases_from_author(author_dir)
        if cases:
            cases_by_author[author] = cases
            all_cases.extend(cases)

    print()
    print(f"Total cases loaded: {len(all_cases)}")
    print(f"Target total: {TARGET_TOTAL}")
    print(f"Progress: {len(all_cases)}/{TARGET_TOTAL} ({len(all_cases)/TARGET_TOTAL*100:.1f}%)")
    print()

    if not all_cases:
        print("No cases found. Exiting.")
        sys.exit(1)

    # Write consolidated file
    output_file = script_dir / "BenchmarkT3_Extension_B.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_cases, f, indent=2, ensure_ascii=False)
    print(f"Wrote consolidated file: {output_file.name} ({len(all_cases)} cases)")
    print()

    # Build statistics
    pearl_by_author = defaultdict(lambda: defaultdict(int))
    difficulty_by_author = defaultdict(lambda: defaultdict(int))
    trap_by_author = defaultdict(lambda: defaultdict(int))
    l3_ground_truth_by_author = defaultdict(lambda: defaultdict(int))
    flags = []
    total_l3_cases = 0

    for author, cases in cases_by_author.items():
        for case in cases:
            pearl_level = case.get("pearl_level", "Unknown")
            difficulty = case.get("difficulty", "Unknown")
            trap_type = case.get("trap", {}).get("type", "Unknown")

            pearl_by_author[pearl_level][author] += 1
            difficulty_by_author[difficulty][author] += 1
            trap_by_author[trap_type][author] += 1

            # Track L3 ground truth
            if pearl_level == "L3":
                total_l3_cases += 1
                # ground_truth can be in hidden_structure or at top level
                ground_truth = case.get("hidden_structure", {}).get("ground_truth")
                if not ground_truth:
                    ground_truth = case.get("ground_truth", "Unknown")
                # Normalize ground truth values
                if ground_truth:
                    ground_truth = ground_truth.upper().strip()
                    # Map common variations
                    if "CONDITION" in ground_truth:
                        ground_truth = "CONDITIONAL"
                    elif "VALID" in ground_truth and "INVALID" not in ground_truth:
                        ground_truth = "VALID"
                    elif "INVALID" in ground_truth:
                        ground_truth = "INVALID"
                else:
                    ground_truth = "Unknown"
                l3_ground_truth_by_author[ground_truth][author] += 1

            # Check for missing fields
            missing = check_mandatory_fields(case)
            if missing:
                flags.append({
                    "author": author,
                    "case_id": case.get("case_id", "?"),
                    "pearl_level": pearl_level,
                    "missing": missing
                })

    # Generate summary report
    authors = sorted(cases_by_author.keys())
    total_cases = len(all_cases)

    report_lines = []
    report_lines.append("# T3 Benchmark Extension B - Analysis Report")
    report_lines.append("")
    report_lines.append(f"**Total Cases:** {total_cases} / {TARGET_TOTAL} ({total_cases/TARGET_TOTAL*100:.1f}%)")
    report_lines.append(f"**Authors:** {', '.join(authors)}")
    report_lines.append(f"**Output File:** BenchmarkT3_Extension_B.json")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # Pearl Level table
    report_lines.append(make_table_with_targets(
        dict(pearl_by_author),
        PEARL_TARGETS,
        row_order=["L1", "L2", "L3"],
        col_order=authors,
        title="Pearl Level Distribution",
        total_cases=total_cases
    ))

    # L3 Ground Truth table (only if there are L3 cases)
    if total_l3_cases > 0:
        report_lines.append(make_l3_ground_truth_table(
            dict(l3_ground_truth_by_author),
            col_order=authors,
            total_l3_cases=total_l3_cases
        ))

    # Difficulty table
    report_lines.append(make_table_with_targets(
        dict(difficulty_by_author),
        DIFFICULTY_TARGETS,
        row_order=["Easy", "Medium", "Hard"],
        col_order=authors,
        title="Difficulty Distribution",
        total_cases=total_cases
    ))

    # Trap Type table
    report_lines.append(make_table_with_targets(
        dict(trap_by_author),
        TRAP_TARGETS,
        col_order=authors,
        title="Trap Type Distribution",
        total_cases=total_cases
    ))

    # Flags table
    report_lines.append(make_flags_table(flags))

    report = "\n".join(report_lines)

    # Write report
    report_file = script_dir / "analysis_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Wrote analysis report: {report_file.name}")
    print()

    # Print summary to console
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print()
    print(report)

    # Return exit code based on flags
    if flags:
        print(f"\nWarning: {len(flags)} cases have missing mandatory fields.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
