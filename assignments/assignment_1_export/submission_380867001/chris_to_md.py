#!/usr/bin/env python3
"""
chris_to_md.py - Convert chris_cases.json to well-formatted markdown

Generates a clean, consistently formatted markdown file from JSON benchmark cases.

Author: Chris Pearce (cases), Converter script generated with Claude Code
"""

import json
import sys
from pathlib import Path


def format_case(case: dict) -> str:
    """Format a single case as markdown."""
    lines = []

    case_id = case.get("case_id", "")
    # Try to extract title from scenario or use a generic one
    scenario = case.get("scenario", "")
    claim = case.get("claim", "")

    # Generate a title from the trap subtype or type
    trap = case.get("trap", {})
    trap_subtype = trap.get("subtype_name") or trap.get("subtype", "")
    trap_type = trap.get("type_name") or trap.get("type", "")
    title = trap_subtype or trap_type or "Economic Case"

    # Case header
    lines.append(f"## **Case {case_id}: {title}**")
    lines.append("")

    # Scenario
    lines.append("**Scenario.**")
    lines.append("")
    lines.append(scenario)
    lines.append("")

    # Claim (if present and different from scenario)
    if claim and claim != scenario:
        lines.append("**Claim.**")
        lines.append("")
        lines.append(f'"{claim}"')
        lines.append("")

    # Variables
    variables = case.get("variables", {})
    lines.append("**Variables.**")
    lines.append("")

    if variables.get("X"):
        x_var = variables["X"]
        x_name = x_var.get("name", "") if isinstance(x_var, dict) else x_var
        x_role = x_var.get("role", "intervention") if isinstance(x_var, dict) else "intervention"
        lines.append(f"- **X** = {x_name} ({x_role.title()})")

    if variables.get("Y"):
        y_var = variables["Y"]
        y_name = y_var.get("name", "") if isinstance(y_var, dict) else y_var
        y_role = y_var.get("role", "outcome") if isinstance(y_var, dict) else "outcome"
        lines.append(f"- **Y** = {y_name} ({y_role.title()})")

    if variables.get("Y0"):
        y0_var = variables["Y0"]
        y0_name = y0_var.get("name", "") if isinstance(y0_var, dict) else y0_var
        lines.append(f"- **Y0** = {y0_name} (Counterfactual Outcome)")

    z_vars = variables.get("Z", [])
    if z_vars:
        for i, z_var in enumerate(z_vars):
            z_name = z_var.get("name", "") if isinstance(z_var, dict) else z_var
            z_role = z_var.get("role", "confounder") if isinstance(z_var, dict) else "confounder"
            # Check if name already has Z prefix
            if z_name.startswith("Z") or z_name.startswith("z"):
                lines.append(f"- **{z_name.split(':')[0].strip()}** = {':'.join(z_name.split(':')[1:]).strip() if ':' in z_name else z_name} ({z_role.replace('_', ' ').title()})")
            else:
                lines.append(f"- **Z{i+1}** = {z_name} ({z_role.replace('_', ' ').title()})")

    lines.append("")

    # Annotations
    lines.append("**Annotations.**")
    lines.append("")
    lines.append(f"- **Case ID:** {case_id}")
    lines.append(f"- **Pearl Level:** {case.get('pearl_level', '')} ({case.get('pearl_level_name', '')})")
    lines.append(f"- **Domain:** {case.get('domain_id', '')} ({case.get('domain_name', '')})")
    lines.append(f"- **Trap Type:** {trap.get('type', '')}")
    if trap.get("subtype"):
        lines.append(f"- **Trap Subtype:** {trap.get('subtype', '')}")
    lines.append(f"- **Difficulty:** {case.get('difficulty', '')}")

    # Causal structure from DAG edges
    hidden = case.get("hidden_structure", {})
    dag_edges = hidden.get("dag_edges", [])
    if dag_edges:
        causal_str = format_dag_edges(dag_edges)
        lines.append(f"- **Causal Structure:** {causal_str}")

    if hidden.get("key_insight"):
        lines.append(f"- **Key Insight:** {hidden['key_insight']}")

    lines.append("")

    # Pearl level specific sections
    pearl_level = case.get("pearl_level", "L1")

    if pearl_level == "L2":
        # Hidden Timestamp
        if hidden.get("hidden_timestamp"):
            lines.append("**Hidden Timestamp.**")
            lines.append("")
            lines.append(hidden["hidden_timestamp"])
            lines.append("")

        # Answer conditions
        if hidden.get("answer_if_tz_lt_tx"):
            lines.append("**Answer if t(Z) < t(X) (Confounder Scenario).**")
            lines.append("")
            lines.append(hidden["answer_if_tz_lt_tx"])
            lines.append("")

        if hidden.get("answer_if_tx_lt_tz"):
            lines.append("**Answer if t(X) < t(Z) (Causal Scenario).**")
            lines.append("")
            lines.append(hidden["answer_if_tx_lt_tz"])
            lines.append("")

    elif pearl_level == "L3":
        # Counterfactual Query
        if hidden.get("counterfactual_query"):
            lines.append("**The Counterfactual Query.**")
            lines.append("")
            lines.append(hidden["counterfactual_query"])
            lines.append("")

        # Counterfactual Structure
        if hidden.get("counterfactual_structure"):
            lines.append("**The Counterfactual Structure.**")
            lines.append("")
            lines.append(hidden["counterfactual_structure"])
            lines.append("")

        # Ground Truth
        if hidden.get("ground_truth"):
            lines.append("**Ground Truth.**")
            lines.append("")
            lines.append(f"**Answer:** {hidden['ground_truth']}")
            lines.append("")
            if case.get("ground_truth_reasoning"):
                lines.append(case["ground_truth_reasoning"])
                lines.append("")

    # Gold Rationale
    if case.get("gold_rationale"):
        lines.append("**Gold Rationale.**")
        lines.append("")
        lines.append(case["gold_rationale"])
        lines.append("")

    # Wise Refusal
    annotation = case.get("annotation", {})
    if annotation.get("wise_refusal"):
        lines.append("**Wise Refusal.**")
        lines.append("")
        lines.append(f'"{annotation["wise_refusal"]}"')
        lines.append("")

    return "\n".join(lines)


def format_dag_edges(edges: list) -> str:
    """Format DAG edges as arrow notation."""
    if not edges:
        return ""

    # Group edges by source to create chains
    from collections import defaultdict
    outgoing = defaultdict(list)
    for source, target in edges:
        outgoing[source].append(target)

    # Simple formatting: just list all edges
    edge_strs = [f"{s} → {t}" for s, t in edges]
    return "; ".join(edge_strs)


def convert_file(input_path: str, output_path: str):
    """Convert JSON file to markdown."""

    # Read input
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        sys.exit(1)

    print(f"Found {len(data)} cases in {input_path}")

    # Generate markdown
    md_lines = []
    md_lines.append("# CS372 Assignment 1 - Economics Benchmark Cases")
    md_lines.append("")
    md_lines.append(f"**Author:** Chris Pearce")
    md_lines.append(f"**Total Cases:** {len(data)}")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

    # Sort cases by case_id
    sorted_cases = sorted(data, key=lambda c: float(c.get("case_id", "0")))

    for case in sorted_cases:
        md_lines.append(format_case(case))
        md_lines.append("---")
        md_lines.append("")

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_lines))

    print(f"Successfully wrote {len(data)} cases to {output_path}")

    # Summary
    from collections import Counter
    pearl_dist = Counter(c["pearl_level"] for c in data)
    print("\nPearl level distribution:")
    for level, count in sorted(pearl_dist.items()):
        print(f"  {level}: {count}")


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    input_file = script_dir / "chris_cases.json"
    output_file = script_dir / "chris_cases.md"

    # Allow command line overrides
    if len(sys.argv) >= 2:
        input_file = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])

    print(f"Converting {input_file} to {output_file}...")
    convert_file(str(input_file), str(output_file))


if __name__ == "__main__":
    main()
