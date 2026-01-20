#!/usr/bin/env python3
"""
Generate Markdown documentation from reviewed_cases.json

Converts JSON benchmark cases to human-readable Markdown format
matching the output_format.md template.

Google Antigravity has been used to generate this script.
"""

import json
from pathlib import Path
from typing import Dict, Any, List


def format_variables(variables: Dict[str, Any]) -> str:
    """Format variables section."""
    lines = []
    
    # X variable
    if 'X' in variables:
        x = variables['X']
        lines.append(f"- **X** = {x.get('name', 'N/A')} ({x.get('role', 'N/A').title()})")
        if x.get('reasoning'):
            lines.append(f"  - *Reasoning:* {x['reasoning']}")
    
    # Y variable
    if 'Y' in variables:
        y = variables['Y']
        lines.append(f"- **Y** = {y.get('name', 'N/A')} ({y.get('role', 'N/A').title()})")
        if y.get('reasoning'):
            lines.append(f"  - *Reasoning:* {y['reasoning']}")
    
    # Z variables
    if 'Z' in variables:
        z_data = variables['Z']
        z_list = z_data if isinstance(z_data, list) else [z_data]
        for i, z in enumerate(z_list, 1):
            z_label = "Z" if len(z_list) == 1 else f"Z{i}"
            lines.append(f"- **{z_label}** = {z.get('name', 'N/A')} ({z.get('role', 'N/A').title()})")
            if z.get('reasoning'):
                lines.append(f"  - *Reasoning:* {z['reasoning']}")
    
    return "\n".join(lines)


def format_annotations(case: Dict[str, Any]) -> str:
    """Format annotations section."""
    lines = []
    
    lines.append(f"- **Case ID:** {case.get('case_id', 'N/A')}")
    lines.append(f"- **Pearl Level:** {case.get('pearl_level', 'N/A')} ({case.get('pearl_level_name', 'N/A')})")
    lines.append(f"- **Domain:** {case.get('domain_id', 'N/A')} ({case.get('domain_name', 'N/A')})")
    
    trap = case.get('trap', {})
    lines.append(f"- **Trap Type:** {trap.get('type', 'N/A')}")
    lines.append(f"- **Trap Subtype:** {trap.get('subtype', 'N/A')}")
    lines.append(f"- **Difficulty:** {case.get('difficulty', 'N/A')}")
    
    # Causal structure from hidden_structure
    hidden = case.get('hidden_structure', {})
    if isinstance(hidden, dict):
        dag_edges = hidden.get('dag_edges', [])
        if dag_edges:
            edges_str = "; ".join([f"{e[0]} → {e[1]}" for e in dag_edges])
            lines.append(f"- **Causal Structure:** {edges_str}")
        
        key_insight = hidden.get('key_insight', '')
        if key_insight:
            lines.append(f"- **Key Insight:** {key_insight}")

    # Suggested Identification Strategy
    id_strategy = case.get('suggested_identification')
    if id_strategy:
        lines.append(f"- **Suggested Identification:** {id_strategy}")
    
    return "\n".join(lines)


def format_hidden_timestamp(case: Dict[str, Any]) -> str:
    """Format hidden timestamp section for L2 cases."""
    hidden = case.get('hidden_structure', {})
    if not isinstance(hidden, dict):
        return ""
    
    timestamp = hidden.get('hidden_timestamp', '')
    if not timestamp:
        return ""
    
    lines = ["\n**Hidden Timestamp.**", "", timestamp]
    
    # Add branched conditional answers
    conditional_answers = hidden.get('conditional_answers', [])
    for ans in conditional_answers:
        condition = ans.get('condition', 'N/A')
        text = ans.get('text', 'N/A')
        lines.append("")
        lines.append(f"**Answer if {condition}.**")
        lines.append(text)
    
    return "\n".join(lines)


def format_case_to_markdown(case: Dict[str, Any]) -> str:
    """Convert a single case to markdown format."""
    lines = []
    
    # Header
    case_num = case.get('case_id', 'Unknown')
    trap_subtype_name = case.get('trap', {}).get('subtype_name', '')
    header = f"## **Case {case_num}: {trap_subtype_name}**" if trap_subtype_name else f"## **Case {case_num}**"
    lines.append(header)
    lines.append("")
    
    # Scenario
    lines.append("**Scenario.**")
    lines.append("")
    lines.append(case.get('scenario', 'N/A'))
    lines.append("")
    
    # Claim
    lines.append("**Claim.**")
    lines.append("")
    claim = case.get('claim', 'N/A')
    lines.append(f'"{claim}"')
    lines.append("")
    
    # Variables
    lines.append("**Variables.**")
    lines.append("")
    lines.append(format_variables(case.get('variables', {})))
    lines.append("")
    
    # Annotations
    lines.append("**Annotations.**")
    lines.append("")
    lines.append(format_annotations(case))
    lines.append("")
    
    # Hidden Timestamp (L2 only)
    hidden_timestamp_section = format_hidden_timestamp(case)
    if hidden_timestamp_section:
        lines.append(hidden_timestamp_section)
        lines.append("")
    
    # Gold Rationale
    lines.append("**Gold Rationale.**")
    lines.append("")
    lines.append(case.get('gold_rationale', 'N/A'))
    lines.append("")
    
    # Wise Refusal
    annotation = case.get('annotation', {})
    wise_refusal = annotation.get('wise_refusal', '')
    if wise_refusal:
        # Strip trailing horizontal rules
        wise_refusal = wise_refusal.strip().rstrip('-').strip()
        lines.append("**Wise Refusal.**")
        lines.append("")
        lines.append(f'"{wise_refusal}"')
        lines.append("")
    
    lines.append("")
    
    return "\n".join(lines)


def main():
    # Paths (relative to this script)
    script_dir = Path(__file__).parent
    input_file = script_dir / "vivek_cases.json"
    output_file = script_dir / "vivek_cases.md"
    
    print(f"Loading cases from {input_file.name}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        cases = json.load(f)
    
    print(f"Loaded {len(cases)} cases")
    
    # Generate markdown
    markdown_lines = [
        "# CS372 Assignment 1 - Economics Benchmark Cases",
        "",
        f"**Author:** Vivek Sathe",
        f"**Total Cases:** {len(cases)}",
        "",
        ""
    ]
    
    print("Converting to markdown...")
    for i, case in enumerate(cases, 1):
        try:
            markdown_lines.append(format_case_to_markdown(case))
            if i % 20 == 0:
                print(f"  Processed {i}/{len(cases)} cases...")
        except Exception as e:
            print(f"ERROR formatting case {case.get('id', i)}: {e}")
    
    # Write output
    markdown_content = "\n".join(markdown_lines)
    
    print(f"Writing to {output_file.name}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✓ Successfully generated {output_file.name}")
    print(f"  Total cases: {len(cases)}")
    print(f"  File size: {len(markdown_content):,} characters")


if __name__ == "__main__":
    main()
