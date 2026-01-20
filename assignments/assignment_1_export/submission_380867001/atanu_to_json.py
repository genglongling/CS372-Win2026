#!/usr/bin/env python3
"""
atanu_to_json.py - Convert atanu.md benchmark cases to JSON format

Converts markdown-formatted T3 benchmark cases to the required JSON schema
for CS372 Assignment 1.

Author: Atanu Mukherjee (cases), Converter script generated with Claude Code
"""

import re
import json
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConversionError:
    """Track conversion errors and warnings"""
    case_id: str
    field: str
    message: str
    severity: str  # "error" or "warning"


@dataclass
class ConversionReport:
    """Summary of conversion results"""
    total_cases: int = 0
    successful: int = 0
    warnings: int = 0
    errors: int = 0
    issues: list = field(default_factory=list)

    def add_issue(self, case_id: str, field: str, message: str, severity: str = "warning"):
        self.issues.append(ConversionError(case_id, field, message, severity))
        if severity == "error":
            self.errors += 1
        else:
            self.warnings += 1

    def print_summary(self):
        print("\n" + "=" * 60)
        print("CONVERSION REPORT")
        print("=" * 60)
        print(f"Total cases processed: {self.total_cases}")
        print(f"Successful conversions: {self.successful}")
        print(f"Cases with warnings: {self.warnings}")
        print(f"Cases with errors: {self.errors}")

        if self.issues:
            print("\n" + "-" * 60)
            print("ISSUES DETECTED:")
            print("-" * 60)
            for issue in self.issues:
                prefix = "[ERROR]" if issue.severity == "error" else "[WARN]"
                print(f"{prefix} Case {issue.case_id} - {issue.field}: {issue.message}")

        print("=" * 60 + "\n")


def split_into_cases(content: str) -> list[tuple[str, str, str]]:
    """Split markdown content into individual cases.

    Returns list of (case_id, title, case_content) tuples.
    """
    # Pattern matches case headers with optional space before colon
    case_pattern = r'\n(?=(?:#+\s*)?\**Case\s+\d)'
    case_blocks = re.split(case_pattern, '\n' + content)

    cases = []
    for block in case_blocks:
        if not block.strip() or "Case" not in block:
            continue

        # Extract case ID and title
        header_match = re.search(r'(?:#+\s*)?\**Case\s*([\d\.]+)\s*:?\s*(.*?)(?:\**|$)', block)
        if header_match:
            case_id = header_match.group(1).strip()
            title = header_match.group(2).strip().rstrip('*')
            cases.append((case_id, title, block))

    return cases


def get_section(block: str, start_marker: str, end_markers: list[str]) -> Optional[str]:
    """Extract content of a named section.

    Args:
        block: The full case content
        start_marker: Name of section to extract (e.g., "Scenario", "Variables")
        end_markers: List of possible next section names to use as boundaries

    Returns:
        Section content or None if not found
    """
    # Normalize escaped characters
    block = block.replace('\\=', '=')
    block = block.replace('\\-', '-')
    block = block.replace('\\<', '<')
    block = block.replace('\\>', '>')

    # Try to find the start marker
    start_pattern = r"\*\*" + re.escape(start_marker) + r"\.?\*\*"
    match = re.search(start_pattern, block, re.IGNORECASE)
    if not match:
        match = re.search(re.escape(start_marker) + r"\.", block, re.IGNORECASE)
    if not match:
        return None

    start_idx = match.end()
    end_idx = len(block)

    # Find the earliest end marker
    for marker in end_markers:
        m_pattern = r"\*\*" + re.escape(marker) + r"\.?\*\*"
        m_match = re.search(m_pattern, block[start_idx:], re.IGNORECASE)
        if m_match:
            idx = start_idx + m_match.start()
            if idx < end_idx:
                end_idx = idx

    return block[start_idx:end_idx].strip()


def parse_variables(var_section: str, report: ConversionReport, case_id: str, pearl_level: str) -> dict:
    """Parse the Variables section into structured format."""
    variables = {"X": None, "Y": None, "Z": [], "Y0": None}

    if not var_section:
        report.add_issue(case_id, "variables", "Variables section not found", "error")
        return variables

    # Normalize escaped characters
    var_section = var_section.replace('\\=', '=')
    var_section = var_section.replace('\\-', '-')
    var_section = var_section.replace('\\<', '<')
    var_section = var_section.replace('\\>', '>')

    # Remove bold markers for simpler parsing
    var_section_clean = re.sub(r'\*\*', '', var_section)

    # Parse line by line
    lines = var_section_clean.split('\n')
    for line in lines:
        line = line.strip().lstrip('•-*').strip()
        if not line:
            continue

        # Pattern: X = description or X: description
        match = re.match(r'^([A-Z][0-9]?)\s*[=:]\s*(.+)', line)
        if not match:
            continue

        var_key = match.group(1).strip()
        var_desc = match.group(2).strip()

        # Extract role from parenthetical suffix like (Treatment), (Outcome), (Mediator)
        role_match = re.search(r'\(([^)]+)\)\s*$', var_desc)
        if role_match:
            role = role_match.group(1).lower().strip()
            name = re.sub(r'\s*\([^)]+\)\s*$', '', var_desc).strip()
        else:
            role = "unknown"
            name = var_desc

        # Map common role names
        role = normalize_role(role)

        v_obj = {"name": name, "role": role}

        if var_key == "X":
            v_obj["role"] = "exposure" if pearl_level == "L1" else "intervention"
            variables["X"] = v_obj
        elif var_key == "Y":
            v_obj["role"] = "outcome"
            variables["Y"] = v_obj
        elif var_key == "Y0":
            v_obj["role"] = "counterfactual_outcome"
            variables["Y0"] = v_obj
        else:
            variables["Z"].append(v_obj)

    # If X or Y not found, try to infer from descriptions
    if not variables["X"] and variables["Z"]:
        for i, z_var in enumerate(variables["Z"]):
            if any(kw in z_var["role"] for kw in ["intervention", "treatment", "exposure"]):
                variables["X"] = variables["Z"].pop(i)
                variables["X"]["role"] = "exposure" if pearl_level == "L1" else "intervention"
                break

    if not variables["Y"] and variables["Z"]:
        for i, z_var in enumerate(variables["Z"]):
            if "outcome" in z_var["role"]:
                variables["Y"] = variables["Z"].pop(i)
                variables["Y"]["role"] = "outcome"
                break

    # Additional fallback: look for common outcome-like variable names (G for growth, etc.)
    if not variables["Y"] and variables["Z"]:
        outcome_keywords = ["growth", "gdp", "outcome", "result", "concentration", "monopoly",
                           "price", "wage", "employment", "profit", "margin"]
        for i, z_var in enumerate(variables["Z"]):
            name_lower = z_var["name"].lower()
            if any(kw in name_lower for kw in outcome_keywords):
                variables["Y"] = variables["Z"].pop(i)
                variables["Y"]["role"] = "outcome"
                break

    # Additional fallback for X: look for first variable if it's clearly the treatment
    if not variables["X"] and variables["Z"]:
        treatment_keywords = ["cost", "policy", "intervention", "treatment", "adoption",
                             "increase", "decrease", "change", "marginal"]
        for i, z_var in enumerate(variables["Z"]):
            name_lower = z_var["name"].lower()
            if any(kw in name_lower for kw in treatment_keywords):
                variables["X"] = variables["Z"].pop(i)
                variables["X"]["role"] = "exposure" if pearl_level == "L1" else "intervention"
                break

    # Validate required variables
    if not variables["X"]:
        report.add_issue(case_id, "variables.X", "X variable not found", "warning")
    if not variables["Y"]:
        report.add_issue(case_id, "variables.Y", "Y variable not found", "warning")
    if not variables["Z"]:
        report.add_issue(case_id, "variables.Z", "No Z variables found", "warning")

    return variables


def normalize_role(role: str) -> str:
    """Normalize role names to standard terms."""
    role_lower = role.lower()
    if any(kw in role_lower for kw in ["treatment", "intervention", "exposure"]):
        return "intervention"
    elif "outcome" in role_lower:
        return "outcome"
    elif "mediator" in role_lower or "intermediate" in role_lower:
        return "mediator"
    elif "confounder" in role_lower or "common" in role_lower:
        return "common_cause"
    elif "collider" in role_lower:
        return "collider"
    elif "selection" in role_lower:
        return "selection"
    elif "counterfactual" in role_lower:
        return "counterfactual_outcome"
    else:
        return role if role != "unknown" else "common_cause"


def parse_annotations(anno_section: str, report: ConversionReport, case_id: str) -> dict:
    """Parse the Annotations section into structured metadata.

    Handles multi-line values like Causal Structure that span multiple lines:
    • **Causal Structure:**
      **U → X**
      **U → Y**
    """
    annotations = {}

    if not anno_section:
        report.add_issue(case_id, "annotations", "Annotations section not found", "warning")
        return annotations

    lines = anno_section.split('\n')
    current_key = None
    current_value_lines = []

    for line in lines:
        original_line = line
        line = line.strip().lstrip('•-*').strip()

        if not line:
            continue

        # Check if this line starts a new key (has colon and starts with a known pattern)
        # Pattern: either "Key:" or "**Key:**"
        key_match = re.match(r'^\*{0,2}([A-Za-z][A-Za-z\s]+?)\*{0,2}\s*:\s*(.*)', line)

        if key_match:
            # Save previous key-value pair
            if current_key:
                annotations[current_key] = '\n'.join(current_value_lines).strip()

            current_key = key_match.group(1).strip().replace('*', '').strip()
            first_val = key_match.group(2).strip().replace('*', '').strip()
            current_value_lines = [first_val] if first_val else []
        elif current_key:
            # This is a continuation line for the current key
            # Remove bold markers and clean up
            clean_line = line.replace('*', '').strip()
            if clean_line:
                current_value_lines.append(clean_line)

    # Don't forget the last key-value pair
    if current_key:
        annotations[current_key] = '\n'.join(current_value_lines).strip()

    return annotations


def extract_claim(block: str, scenario: str) -> str:
    """Extract the claim from the case content."""
    # Try explicit claim patterns first
    claim_patterns = [
        r'(?:claim|claims|Management asks|Policymakers claim|policymaker\'s claim):\s*[""\']?(.*?)[""\']?(?:\n|$)',
        r'(?:concludes?|argues?|asserts?)(?:\s+that)?:\s*[""\']?(.*?)[""\']?(?:\n|$)',
        r'"([^"]+)"(?:\s*$|\s*\n)',  # Quoted statement at end
    ]

    for pattern in claim_patterns:
        match = re.search(pattern, block, re.IGNORECASE | re.MULTILINE)
        if match:
            claim = match.group(1).strip().strip('""\'"')
            if len(claim) > 20:  # Sanity check
                return claim

    # Fallback: last sentence of scenario
    if scenario:
        sentences = re.split(r'(?<=[.!?])\s+', scenario)
        if sentences:
            return sentences[-1].strip()

    return "[CLAIM NOT FOUND]"


def parse_dag_edges(causal_structure: str) -> list[list[str]]:
    """Parse causal structure notation into DAG edges.

    Handles patterns like:
    - X → Y
    - X → M → Y (chain)
    - X → K ← U (collider, note: ← means reverse direction)
    - U → Z₁, Z₂ → Y (multiple targets)
    - X → Z → Y independently (ignore trailing text)
    """
    edges = []

    if not causal_structure:
        return edges

    # Normalize unicode subscripts to regular numbers
    subscript_map = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
                     '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9'}
    for sub, num in subscript_map.items():
        causal_structure = causal_structure.replace(sub, num)

    # Process each line/chain
    for chain in causal_structure.split('\n'):
        chain = chain.strip()
        if not chain:
            continue

        # Skip lines that are just comments or don't have arrows
        if '→' not in chain and '->' not in chain and '←' not in chain and '<-' not in chain:
            continue

        # Remove trailing commentary (e.g., "independently", "with conditioning on K")
        chain = re.sub(r',?\s*with\s+.*$', '', chain, flags=re.IGNORECASE)
        chain = re.sub(r'\s+independently\s*$', '', chain, flags=re.IGNORECASE)
        chain = re.sub(r'\s+or\s*$', '', chain, flags=re.IGNORECASE)

        # Find all arrows and their directions
        # Split into segments between arrows
        segments = re.split(r'\s*(->|→|←|<-)\s*', chain)

        # segments will be like: ['X', '→', 'M', '→', 'Y'] or ['X', '←', 'Z']
        if len(segments) < 3:
            continue

        i = 0
        while i < len(segments) - 2:
            left_raw = segments[i].strip()
            arrow = segments[i + 1]
            right_raw = segments[i + 2].strip()

            # Extract node names (capital letters and numbers only)
            # Handle comma-separated nodes like "Z1, Z2"
            left_nodes = re.findall(r'[A-Z][A-Z0-9]*', left_raw.upper())
            right_nodes = re.findall(r'[A-Z][A-Z0-9]*', right_raw.upper())

            # Determine direction
            is_reverse = arrow in ['←', '<-']

            # Create edges
            for left in left_nodes:
                for right in right_nodes:
                    if left and right:
                        if is_reverse:
                            edges.append([right, left])
                        else:
                            edges.append([left, right])

            i += 2

    # Deduplicate edges while preserving order
    seen = set()
    unique_edges = []
    for edge in edges:
        key = tuple(edge)
        if key not in seen:
            seen.add(key)
            unique_edges.append(edge)

    return unique_edges


def get_trap_type_name(trap_type: str) -> str:
    """Get human-readable trap type name."""
    names = {
        'CONF-MED': 'Confounding via Mediator',
        'COUNTERFACTUAL': 'Counterfactual Reasoning Error',
        'COLLIDER': 'Collider Bias',
        'SELECTION': 'Selection Bias',
        'REVERSE': 'Reverse Causation / Endogeneity',
        'MECHANISM': 'Mechanism / Supply-Demand Logic',
        'MED': 'Mediation Effect',
        'SIMPSONS': "Simpson's Paradox",
        'SURVIVORSHIP': 'Survivorship Bias',
        'GOODHART': "Goodhart's Law",
        'CONF-MED-COLLIDER': 'Confounding via Mediator with Collider',
    }
    return names.get(trap_type, trap_type)


def convert_case(case_id: str, title: str, content: str, report: ConversionReport) -> Optional[dict]:
    """Convert a single case from markdown to JSON format."""

    # Define section markers for extraction
    markers = ["Scenario", "Variables", "Annotations", "Hidden Timestamp",
               "The Counterfactual Query", "The Counterfactual Structure",
               "Correct Reasoning", "Ground Truth", "Wise Refusal", "Answer"]

    # Extract sections
    scenario = get_section(content, "Scenario", markers[1:]) or ""
    variables_txt = get_section(content, "Variables", markers[2:]) or ""
    annotations_txt = get_section(content, "Annotations", markers[3:]) or ""

    if not scenario:
        report.add_issue(case_id, "scenario", "Scenario not found", "error")
        return None

    # Parse annotations
    annotations = parse_annotations(annotations_txt, report, case_id)

    # Determine Pearl level
    pearl_level_raw = annotations.get("Pearl Level", "L1")
    if "L3" in pearl_level_raw:
        pearl_level, pl_name = "L3", "Counterfactual"
    elif "L2" in pearl_level_raw:
        pearl_level, pl_name = "L2", "Intervention"
    else:
        pearl_level, pl_name = "L1", "Association"

    # Use Case ID from annotations if available, otherwise use parsed ID
    case_id_final = annotations.get("Case ID", case_id)

    # Parse variables
    variables = parse_variables(variables_txt, report, case_id, pearl_level)

    # Extract claim
    claim = extract_claim(content, scenario)

    # Get trap info
    trap_type = annotations.get("Trap Type", "NONE")
    trap_type = trap_type.upper().replace(' ', '-')
    trap_subtype = annotations.get("Trap Subtype", "")

    # Parse DAG edges
    causal_structure = annotations.get("Causal Structure", "")
    dag_edges = parse_dag_edges(causal_structure)

    # Get key insight
    key_insight = annotations.get("Key Insight", "")

    # Get difficulty
    difficulty = annotations.get("Difficulty", "Medium")
    difficulty = difficulty.strip().capitalize()
    if difficulty not in ["Easy", "Medium", "Hard"]:
        difficulty = "Medium"

    # Build base case structure
    case = {
        "id": f"T3-BucketLarge-B-{case_id_final}",
        "bucket": "BucketLarge-B",
        "case_id": case_id_final,
        "pearl_level": pearl_level,
        "pearl_level_name": pl_name,
        "domain_id": "D5",
        "domain_name": "Economics",
        "scenario": scenario,
        "claim": claim,
        "label": "NO",
        "label_name": "FLAWED",
        "is_ambiguous": False,
        "trap": {
            "type": trap_type,
            "type_name": get_trap_type_name(trap_type),
            "subtype": trap_subtype,
            "subtype_name": trap_subtype.replace('_', ' ').title() if trap_subtype else ""
        },
        "variables": variables,
        "hidden_structure": {
            "dag_edges": dag_edges,
            "notes": causal_structure,
            "key_insight": key_insight
        },
        "gold_rationale": key_insight or f"See detailed analysis in case {case_id}",
        "difficulty": difficulty,
        "source": {
            "origin": "generated",
            "file": "atanu.md",
            "generator": "llm_generated"
        },
        "annotation": {
            "author": "Atanu Mukherjee",
            "num_annotators": 1,
            "agreement": "generated",
            "adjudicated": True
        }
    }

    # Handle L3 (Counterfactual) specific fields
    if pearl_level == "L3":
        gt_section = get_section(content, "Ground Truth", ["Wise Refusal"]) or ""

        # Determine label from ground truth
        gt_upper = gt_section.upper()
        if "CONDITIONAL" in gt_upper:
            case["label"] = "MAYBE"
            case["label_name"] = "CONDITIONAL"
            case["is_ambiguous"] = True
        elif "YES" in gt_upper or "VALID" in gt_upper:
            case["label"] = "YES"
            case["label_name"] = "VALID"
        else:
            case["label"] = "NO"
            case["label_name"] = "INVALID"

        # Get counterfactual query
        cf_query = get_section(content, "The Counterfactual Query", ["Correct Reasoning", "Ground Truth"])
        if not cf_query:
            cf_query = get_section(content, "The Counterfactual Structure", ["Correct Reasoning", "Ground Truth"])

        case["hidden_structure"]["counterfactual_query"] = cf_query or ""
        case["hidden_structure"]["ground_truth"] = gt_section

        # Get correct reasoning
        correct_reasoning = get_section(content, "Correct Reasoning", ["Ground Truth", "Wise Refusal"])
        if correct_reasoning:
            case["ground_truth_reasoning"] = correct_reasoning

        # Ensure Y0 exists for L3
        if not variables.get("Y0") and variables.get("Y"):
            case["variables"]["Y0"] = {
                "name": f"Counterfactual outcome for {variables['Y']['name']}",
                "role": "counterfactual_outcome"
            }

    # Handle L2 (Intervention) specific fields
    elif pearl_level == "L2":
        # Default to NO/FLAWED for L2
        case["label"] = "NO"
        case["label_name"] = "FLAWED"

        # Get hidden timestamp
        hidden_ts = get_section(content, "Hidden Timestamp", ["Answer"]) or ""
        case["hidden_structure"]["hidden_timestamp"] = hidden_ts

        # Extract answer conditions
        answers = re.findall(r'\**Answer\s+(.*?)\.?\**\s*\n(.*?)(?=\**Answer|\**Wise Refusal|$)',
                            content, re.DOTALL | re.IGNORECASE)

        if len(answers) >= 1:
            case["hidden_structure"]["answer_if_tx_lt_tz"] = answers[0][1].strip()
        if len(answers) >= 2:
            case["hidden_structure"]["answer_if_tz_lt_tx"] = answers[1][1].strip()

    # Handle L1 (Association) specific fields
    else:
        case["label"] = "NO"
        case["label_name"] = "FLAWED"
        if variables.get("X"):
            variables["X"]["role"] = "exposure"

    # Get wise refusal
    wise_refusal = get_section(content, "Wise Refusal", ["###", "##"]) or ""
    case["annotation"]["wise_refusal"] = wise_refusal

    return case


def convert_file(input_path: str, output_path: str) -> ConversionReport:
    """Convert the entire markdown file to JSON."""
    report = ConversionReport()

    # Read input file
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    # Split into cases
    cases = split_into_cases(content)
    report.total_cases = len(cases)

    print(f"Found {len(cases)} cases in {input_path}")

    # Convert each case
    converted_cases = []
    for case_id, title, case_content in cases:
        print(f"Processing case {case_id}: {title[:50]}...")

        try:
            case_json = convert_case(case_id, title, case_content, report)
            if case_json:
                converted_cases.append(case_json)
                report.successful += 1
        except Exception as e:
            import traceback
            report.add_issue(case_id, "conversion", f"Exception: {e}\n{traceback.format_exc()}", "error")

    # Write output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(converted_cases, f, indent=2, ensure_ascii=False)
        print(f"\nSuccessfully wrote {len(converted_cases)} cases to {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

    return report


def main():
    """Main entry point."""
    # Default paths
    script_dir = Path(__file__).parent
    input_file = script_dir / "atanu_cases.md"
    output_file = script_dir / "atanu_cases.json"

    # Allow command line overrides
    if len(sys.argv) >= 2:
        input_file = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])

    print(f"Converting {input_file} to {output_file}...")

    # Run conversion
    report = convert_file(str(input_file), str(output_file))

    # Print report
    report.print_summary()

    # Return exit code based on errors
    if report.errors > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
