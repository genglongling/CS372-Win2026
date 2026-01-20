#!/usr/bin/env python3
"""
Generate descriptive statistics from the JSON dataset and output to markdown report.
"""

import json
import re
import pandas as pd
from collections import defaultdict

def extract_case_titles(markdown_file):
    """Extract case titles from markdown headings and match with case_ids."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match headings followed by code blocks with JSON
    # Match: # Title\n\n```python\n{... "case_id": "X.Y" ...}
    pattern = r'#\s+(.+?)\n\n```python\s*\{[^}]*"case_id":\s*"([^"]+)"'
    matches = re.findall(pattern, content, re.DOTALL)
    
    title_map = {}
    for title, case_id in matches:
        # Clean up title - remove special characters, make it compact
        clean_title = title.strip()
        title_map[case_id] = clean_title
    
    return title_map

def map_pearl_level_to_code(pearl_level_name):
    """Map pearl level name to code (L1, L2, L3)."""
    mapping = {
        "Association": "L1",
        "Intervention": "L2",
        "Counterfactual": "L3"
    }
    return mapping.get(pearl_level_name, pearl_level_name)

def shorten_difficulty(diff):
    """Shorten difficulty names (Medium -> Med)."""
    if diff == "Medium":
        return "Med"
    return diff

def shorten_trap_type(trap_type):
    """Shorten trap type names for display."""
    # Handle specific cases first
    replacements = {
        "REGRESSION_TO_MEAN": "REGRESSIONTOM",
        "BASE_RATE_NEGLECT": "BASERATENEGLE",
        "OMITTED_VARIABLE": "OMITTEDVARIABL",
        "SELECTION_BIAS": "SELECTIONBIAS",
        "CONFOUNDING_MEDIATOR": "CONF-MED",
        "CONFOUNDING": "CONF-MED",
        "CONF_MED": "CONF-MED",
        "CAUSAL_ORDER": "CAUSALORDER"
    }
    
    # Check exact match first
    if trap_type in replacements:
        return replacements[trap_type]
    
    # Check if it starts with any replacement key
    for full, short in replacements.items():
        if trap_type.startswith(full):
            return short
    
    # Remove underscores for other cases
    shortened = trap_type.replace("_", "")
    
    # Truncate if too long
    if len(shortened) > 15:
        return shortened[:15]
    return shortened

def generate_statistics(dataset_file, markdown_file, output_file):
    """Generate descriptive statistics and save to markdown."""
    
    # Load dataset
    with open(dataset_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract case titles
    title_map = extract_case_titles(markdown_file)
    
    # Convert to DataFrame
    records = []
    for item in data:
        record = {
            'case_id': item.get('case_id', ''),
            'case_title': title_map.get(item.get('case_id', ''), item.get('case_id', '')),
            'pearl_level': item.get('pearl_level', ''),
            'pearl_level_name': item.get('pearl_level_name', ''),
            'difficulty': item.get('difficulty', ''),
            'trap_type': item.get('trap', {}).get('type', '') if isinstance(item.get('trap'), dict) else '',
            'label': item.get('label', '')
        }
        records.append(record)
    
    df = pd.DataFrame(records)
    
    # Generate markdown report
    report = []
    report.append("# Descriptive Statistics Report\n")
    
    # Pearl Level Summary Table
    report.append("## Pearl Level Summary Tables\n")
    
    # Group by pearl level
    for level_name in ["Association", "Intervention", "Counterfactual"]:
        level_df = df[df['pearl_level_name'] == level_name].copy()
        if len(level_df) == 0:
            continue
        
        level_code = map_pearl_level_to_code(level_name)
        report.append(f"### {level_name} ({level_code})\n")
        
        # Prepare table data
        table_data = []
        for _, row in level_df.iterrows():
            trap_short = shorten_trap_type(row['trap_type'])
            diff_short = shorten_difficulty(row['difficulty'])
            title_short = row['case_title'][:30] + "..." if len(row['case_title']) > 30 else row['case_title']
            
            table_data.append({
                'Case': row['case_id'],
                'Title': title_short,
                'TrapType': trap_short,
                'Level': level_code,
                'Diff': diff_short
            })
        
        # Sort by case_id
        table_data.sort(key=lambda x: float(x['Case']))
        
        # Create markdown table
        report.append("| Case | Title | TrapType | Level | Diff |")
        report.append("|------|-------|----------|-------|------|")
        for item in table_data:
            report.append(f"| {item['Case']} | {item['Title']} | {item['TrapType']} | {item['Level']} | {item['Diff']} |")
        report.append("")
    
    # Distributions
    report.append("## Distributions\n")
    
    # Pearl Level Distribution
    report.append("### Pearl Level Distribution\n")
    pearl_counts = df['pearl_level_name'].value_counts().sort_index()
    total = len(df)
    for level_name, count in pearl_counts.items():
        level_code = map_pearl_level_to_code(level_name)
        pct = (count / total) * 100
        report.append(f"- {level_code} ({level_name}): {count} cases ({pct:.0f}%)")
    report.append(f"- Total: {total} cases\n")
    
    # Label Distribution (All Examples)
    report.append("### Label Distribution (All Examples)\n")
    label_counts = df['label'].value_counts()
    for label, count in label_counts.items():
        pct = (count / total) * 100
        report.append(f"- {label}: {count} cases ({pct:.0f}%)")
    report.append("")
    
    # L3 Ground Truth Distribution
    report.append("### L3 Ground Truth Distribution\n")
    l3_df = df[df['pearl_level_name'] == 'Counterfactual']
    if len(l3_df) > 0:
        l3_label_counts = l3_df['label'].value_counts()
        l3_total = len(l3_df)
        for label, count in l3_label_counts.items():
            pct = (count / l3_total) * 100
            # Get case_ids for this label
            case_ids = sorted(l3_df[l3_df['label'] == label]['case_id'].tolist(), 
                            key=lambda x: float(x))
            case_ids_str = ", ".join(case_ids)
            report.append(f"- {label}: {count} cases ({pct:.0f}%) — {case_ids_str}")
    report.append("")
    
    # Trap Type Distribution
    report.append("### Trap Type Distribution\n")
    trap_counts = df['trap_type'].value_counts()
    for trap_type, count in trap_counts.items():
        pct = (count / total) * 100
        trap_short = shorten_trap_type(trap_type)
        report.append(f"- {trap_short}: {count} cases ({pct:.0f}%)")
    report.append("")
    
    # Difficulty Distribution
    report.append("### Difficulty Distribution\n")
    diff_counts = df['difficulty'].value_counts()
    for difficulty, count in diff_counts.items():
        pct = (count / total) * 100
        report.append(f"- {difficulty}: {count} cases ({pct:.0f}%)")
    report.append("")
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"Statistics report generated: {output_file}")
    print(f"Total cases analyzed: {total}")

if __name__ == "__main__":
    dataset_file = "dataset.json"
    markdown_file = "claude_generated_jsons.md"
    output_file = "statistics_report.md"
    
    generate_statistics(dataset_file, markdown_file, output_file)

