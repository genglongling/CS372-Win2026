#!/usr/bin/env python3
"""
Parse vivek_cases.md and convert back to JSON matching target_schema.json

Parses the markdown format and reconstructs the JSON benchmark cases.

Google Antigravity has been used to generate this script. 
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional


def parse_markdown_to_json(md_content: str) -> List[Dict[str, Any]]:
    """Parse markdown content into JSON cases."""
    
    cases = []
    
    # Split by case headers (## **Case ...)
    case_blocks = re.split(r'\n## \*\*Case ([^*]+)\*\*\n', md_content)
    
    # Skip the header (first element before first case)
    for i in range(1, len(case_blocks), 2):
        if i + 1 >= len(case_blocks):
            break
            
        case_header = case_blocks[i].strip()
        case_content = case_blocks[i + 1].strip()
        
        try:
            case = parse_single_case(case_header, case_content)
            if case:
                cases.append(case)
        except Exception as e:
            print(f"ERROR parsing case {case_header}: {e}")
            continue
    
    return cases


def parse_single_case(header: str, content: str) -> Optional[Dict[str, Any]]:
    """Parse a single case block."""
    
    case = {}
    
    # Extract case_id from header (e.g., "Gen1.1-VarA: Omitted Variable")
    case_id_match = re.match(r'^([^:]+)', header)
    if case_id_match:
        case_id = case_id_match.group(1).strip()
        case['case_id'] = case_id
        case['id'] = f"T3-BucketLarge-B-{case_id}"
    else:
        return None
    
    case['bucket'] = "BucketLarge-B"
    
    # Parse sections
    sections = {}
    current_section = None
    current_content = []
    
    for line in content.split('\n'):
        # Check for section headers
        if line.startswith('**') and line.endswith('.**'):
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line.strip('*').strip('.')
            current_content = []
        else:
            current_content.append(line)
    
    # Add last section
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    # Extract scenario
    case['scenario'] = sections.get('Scenario', '').strip()
    
    # Extract claim (remove quotes)
    claim_raw = sections.get('Claim', '').strip()
    case['claim'] = claim_raw.strip('"').strip()
    
    # Parse variables
    case['variables'] = parse_variables(sections.get('Variables', ''))
    
    # Parse annotations
    annotations_text = sections.get('Annotations', '')
    parse_annotations(case, annotations_text)
    
    # Parse hidden_structure
    case['hidden_structure'] = parse_hidden_structure(
        annotations_text,
        sections.get('Hidden Timestamp', ''),
        case.get('pearl_level', '')
    )
    
    # Extract gold_rationale
    case['gold_rationale'] = sections.get('Gold Rationale', '').strip()
    
    # Extract wise_refusal
    wise_refusal = sections.get('Wise Refusal', '').strip().strip('"')
    
    # Set difficulty
    case['difficulty'] = case.get('difficulty', 'Medium')
    
    # Set source
    case['source'] = {
        "origin": "human_annotator",
        "file": "vivek_cases.md",
        "generator": "human"
    }
    
    # Set annotation
    case['annotation'] = {
        "author": case.get('author', 'Vivek Sathe'),
        "num_annotators": 1,
        "agreement": "human_endorsed",
        "adjudicated": True,
        "wise_refusal": wise_refusal if wise_refusal else "Additional information needed for evaluation."
    }
    
    # Add ground_truth_reasoning for L3 cases
    if 'L3' in case.get('pearl_level', '') or 'Counterfactual' in case.get('pearl_level_name', ''):
        case['ground_truth_reasoning'] = case.get('gold_rationale', '')
    
    return case


def parse_variables(variables_text: str) -> Dict[str, Any]:
    """Parse variables section."""
    variables = {}
    
    lines = variables_text.strip().split('\n')
    z_list = []
    
    for line in lines:
        line = line.strip()
        if not line or not line.startswith('- **'):
            continue
        
        # Parse format: - **X** = Name (Role)
        match = re.match(r'- \*\*([XYZ]\d*)\*\* = ([^(]+)\(([^)]+)\)', line)
        if match:
            var_name = match.group(1)
            var_desc = match.group(2).strip()
            var_role = match.group(3).strip().lower().replace(' ', '_')
            
            if var_name.startswith('Z'):
                z_list.append({"name": var_desc, "role": var_role})
            else:
                variables[var_name] = {"name": var_desc, "role": var_role}
    
    if z_list:
        variables['Z'] = z_list
    
    return variables


def parse_annotations(case: Dict[str, Any], annotations_text: str):
    """Parse annotations section and populate case fields."""
    
    for line in annotations_text.split('\n'):
        line = line.strip()
        if not line.startswith('- **'):
            continue
        
        # Parse format: - **Field:** Value
        match = re.match(r'- \*\*([^:]+):\*\* (.+)', line)
        if not match:
            continue
        
        field = match.group(1).strip()
        value = match.group(2).strip()
        
        if field == 'Pearl Level':
            # Parse "L2 (Intervention)"
            pearl_match = re.match(r'(L\d+)\s*\(([^)]+)\)', value)
            if pearl_match:
                case['pearl_level'] = pearl_match.group(1)
                case['pearl_level_name'] = pearl_match.group(2)
        elif field == 'Domain':
            # Parse "D5 (Economics)"
            domain_match = re.match(r'(D\d+)\s*\(([^)]+)\)', value)
            if domain_match:
                case['domain_id'] = domain_match.group(1)
                case['domain_name'] = domain_match.group(2)
        elif field == 'Trap Type':
            if 'trap' not in case:
                case['trap'] = {}
            case['trap']['type'] = value
        elif field == 'Trap Subtype':
            if 'trap' not in case:
                case['trap'] = {}
            case['trap']['subtype'] = value
            case['trap']['subtype_name'] = value.replace('_', ' ')
        elif field == 'Difficulty':
            case['difficulty'] = value
        elif field == 'Causal Structure':
            # Will be used in hidden_structure
            case['_causal_structure'] = value
    
    # Set defaults
    if 'trap' in case:
        if 'type_name' not in case['trap']:
            case['trap']['type_name'] = case['trap'].get('type', '').replace('_', ' ').title()
    
    # Set label based on claim validity
    case['label'] = case.get('label', 'NO')
    case['label_name'] = case.get('label_name', 'FLAWED')
    case['is_ambiguous'] = case.get('is_ambiguous', False)


def parse_hidden_structure(annotations_text: str, hidden_timestamp: str, pearl_level: str) -> Dict[str, Any]:
    """Parse hidden structure."""
    
    hidden = {
        "dag_edges": [["X", "Y"]],  # Default
        "notes": "",
        "key_insight": ""
    }
    
    # Extract key insight from annotations
    for line in annotations_text.split('\n'):
        if '**Key Insight:**' in line:
            insight = line.split('**Key Insight:**', 1)[1].strip()
            hidden['key_insight'] = insight
            hidden['notes'] = insight[:500] if len(insight) > 500 else insight
            break
    
    # Extract causal structure and convert to dag_edges
    for line in annotations_text.split('\n'):
        if '**Causal Structure:**' in line:
            struct = line.split('**Causal Structure:**', 1)[1].strip()
            # Parse arrows like "X → Z1; Z1 → Y" or "X -> Z1"
            edges = []
            for edge_str in struct.split(';'):
                # Match any arrow: →, ->, -->, etc.
                edge_match = re.findall(r'([A-Z]\d*)\s*(?:→|->|—>|-->)\s*([A-Z]\d*)', edge_str)
                edges.extend([[m[0], m[1]] for m in edge_match])
            if edges:
                hidden['dag_edges'] = edges
            break
    
    # Add hidden timestamp for L2
    if hidden_timestamp and ('L2' in pearl_level or 'Intervention' in pearl_level):
        hidden['hidden_timestamp'] = hidden_timestamp.strip()
    
    return hidden


def compare_json_files(file1_path: Path, file2_path: Path):
    """Compare two JSON files and report differences."""
    
    with open(file1_path, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    
    with open(file2_path, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    
    print(f"\n{'='*60}")
    print("JSON COMPARISON")
    print(f"{'='*60}")
    print(f"File 1: {file1_path.name} ({len(data1)} cases)")
    print(f"File 2: {file2_path.name} ({len(data2)} cases)")
    print()
    
    # Compare counts
    if len(data1) != len(data2):
        print(f"⚠️  Different number of cases: {len(data1)} vs {len(data2)}")
    else:
        print(f"✓ Same number of cases: {len(data1)}")
    
    # Compare first case structure
    if data1 and data2:
        keys1 = set(data1[0].keys())
        keys2 = set(data2[0].keys())
        
        print(f"\nFirst case field comparison:")
        print(f"  File 1 fields: {sorted(keys1)}")
        print(f"  File 2 fields: {sorted(keys2)}")
        
        if keys1 == keys2:
            print(f"  ✓ Same fields")
        else:
            only_in_1 = keys1 - keys2
            only_in_2 = keys2 - keys1
            if only_in_1:
                print(f"  ⚠️  Only in {file1_path.name}: {only_in_1}")
            if only_in_2:
                print(f"  ⚠️  Only in {file2_path.name}: {only_in_2}")


def main():
    # Paths (relative to this script)
    script_dir = Path(__file__).parent
    md_file = script_dir / "vivek_cases.md"
    output_file = script_dir / "vivek_cases.json"
    reference_file = script_dir / "reviewed_cases.json"
    
    print(f"Reading {md_file.name}...")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print("Parsing markdown...")
    cases = parse_markdown_to_json(md_content)
    
    print(f"Parsed {len(cases)} cases")
    
    print(f"Writing to {output_file.name}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cases, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Successfully created {output_file.name}")
    
    # Compare with reference
    if reference_file.exists():
        compare_json_files(output_file, reference_file)
    
    print(f"\n{'='*60}")
    print("DONE")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
