# COMMAND ----------
#!/usr/bin/env python3
"""
Data Generation Script for CS372 Assignment 1 - Group F
History & Geopolitics Domain (Bucket F)

This script generates 80 new cases following the T� Benchmark structure,
maintaining the distribution:
- L1 (Association): 9 cases
- L2 (Intervention): 53 cases
- L3 (Counterfactual): 18 cases (VALID=5, INVALID=5, CONDITIONAL=8)
"""

# export OPENAI_API_KEY='sk-2-8GQgLxh_M0Ki2t0s1r6g'
# export OPENAI_API_KEY='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'

import json
import os
from openai import OpenAI
from typing import Dict, List, Any
import random

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Target quotas based on assignment
PEARL_QUOTAS = {
    "L1": 9,
    "L2": 53,
    "L3": 18
}

L3_GROUND_TRUTH_QUOTAS = {
    "VALID": 5,
    "INVALID": 5,
    "CONDITIONAL": 8
}

TRAP_TYPES = ["CONF-MED", "REVERSE", "SELECTION", "COLLIDER", "COUNTERFACTUAL",
              "SPURIOUS", "BASE_RATE", "SIMPSON", "ECOLOGICAL"]

SUBDOMAINS = [
    "Economic History", "Military History", "Political History",
    "Ancient History", "Medieval History", "Early Modern History",
    "Diplomatic History", "Social History", "Historiography",
    "Archival Studies", "Historical Methodology"
]

def generate_case(pearl_level: str, target_trap: str, l3_ground_truth: str = None, case_id: int = 1) -> Dict[str, Any]:
    """Generate a single case using OpenAI API"""

    prompt = f"""Generate a historical reasoning case for the T� Benchmark.

Domain: History & Geopolitics (D2)
Pearl Level: {pearl_level}
Target Trap Type: {target_trap}
{"Ground Truth Label: " + l3_ground_truth if l3_ground_truth else ""}

Requirements:
1. Create a unique historical scenario that tests causal reasoning
2. Focus on {"Association" if pearl_level == "L1" else "Intervention" if pearl_level == "L2" else "Counterfactual"} reasoning
3. The scenario should clearly demonstrate the {target_trap} trap
4. Use variables X (treatment/event), Y (outcome), Z (confounder/mediator)
5. Provide a "wise refusal" response that explains the causal trap

Output ONLY valid JSON with this exact structure:
{{
    "case_id": "F.{case_id}",
    "domain": "D2",
    "pearl_level": "{pearl_level}",
    "trap_type": "{target_trap}",
    "trap_subtype": "<specific subtype>",
    "difficulty": "<Easy/Medium/Hard>",
    "subdomain": "<specific historical subdomain>",
    "scenario": "<historical scenario description>",
    "variables": {{
        "X": "<variable description>",
        "Y": "<outcome description>",
        "Z": "<confounding variable description>"
    }},
    "user_question": "<question asking about the causal relationship>",
    "expected_reasoning": "{"Association" if pearl_level == "L1" else "Intervention" if pearl_level == "L2" else "Counterfactual"}",
    "reference_answer": "<correct causal analysis>",
    "wise_refusal": "<explanation of why the naive causal claim is wrong>"
    {"," + '"ground_truth": "' + l3_ground_truth + '"' if l3_ground_truth else ""}
}}

Make the scenario novel and different from common examples. Focus on less-known historical events."""

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # More reliable for structured JSON output
            messages=[
                {"role": "system", "content": "You are an expert in causal inference and historical analysis. Generate precise, well-structured causal reasoning cases in valid JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=1500
        )

        content = response.choices[0].message.content.strip()

        # Extract JSON if wrapped in markdown code blocks
        if content.startswith("```"):
            lines = content.split("\n")
            # Remove first and last lines (``` markers)
            content = "\n".join(lines[1:-1]) if len(lines) > 2 else content
            if content.startswith("json"):
                content = content[4:].strip()

        content = content.strip()

        # Debug: print first 100 chars if parsing fails
        if not content:
            print(f"    ⚠ Empty response from model")
            return None

        case = json.loads(content)
        return case
    except json.JSONDecodeError as e:
        print(f"    ⚠ JSON parsing error: {e}")
        print(f"    First 200 chars of response: {content[:200] if content else 'empty'}")
        return None
    except Exception as e:
        print(f"    ⚠ Error generating case: {e}")
        return None

def validate_case(case: Dict[str, Any]) -> bool:
    """Validate case has all required fields"""
    required_fields = ["case_id", "domain", "pearl_level", "trap_type", "scenario",
                      "variables", "user_question", "reference_answer", "wise_refusal"]

    if not all(field in case for field in required_fields):
        return False

    if not all(var in case["variables"] for var in ["X", "Y", "Z"]):
        return False

    return True

def generate_dataset(output_file: str = "group_F.json"):
    """Generate the complete dataset"""
    dataset = []
    case_counter = 1

    print("Generating T� Benchmark Dataset for Group F (History & Geopolitics)")
    print("=" * 70)

    # Generate L1 cases
    print(f"\nGenerating L1 (Association) cases: {PEARL_QUOTAS['L1']}")
    l1_traps = ["SPURIOUS", "BASE_RATE", "SELECTION", "SIMPSON", "ECOLOGICAL"]
    for i in range(PEARL_QUOTAS['L1']):
        trap = random.choice(l1_traps)
        print(f"  Case {case_counter}: L1 - {trap}")
        case = generate_case("L1", trap, case_id=case_counter)
        if case and validate_case(case):
            dataset.append(case)
            case_counter += 1
            # Save after each successful case
            with open(output_file, 'w') as f:
                json.dump(dataset, f, indent=2)
            print(f"    ✓ Saved ({len(dataset)} total)")
        else:
            print(f"    ⚠ Failed to generate valid case, retrying...")
            i -= 1

    # Generate L2 cases
    print(f"\nGenerating L2 (Intervention) cases: {PEARL_QUOTAS['L2']}")
    l2_traps = ["CONF-MED", "REVERSE", "SELECTION", "COLLIDER"]
    for i in range(PEARL_QUOTAS['L2']):
        trap = random.choice(l2_traps)
        print(f"  Case {case_counter}: L2 - {trap}")
        case = generate_case("L2", trap, case_id=case_counter)
        if case and validate_case(case):
            dataset.append(case)
            case_counter += 1
            # Save after each successful case
            with open(output_file, 'w') as f:
                json.dump(dataset, f, indent=2)
            print(f"    ✓ Saved ({len(dataset)} total)")
        else:
            print(f"    ⚠ Failed to generate valid case, retrying...")
            i -= 1

    # Generate L3 cases
    print(f"\nGenerating L3 (Counterfactual) cases: {PEARL_QUOTAS['L3']}")
    l3_ground_truths = (
        ["VALID"] * L3_GROUND_TRUTH_QUOTAS["VALID"] +
        ["INVALID"] * L3_GROUND_TRUTH_QUOTAS["INVALID"] +
        ["CONDITIONAL"] * L3_GROUND_TRUTH_QUOTAS["CONDITIONAL"]
    )
    random.shuffle(l3_ground_truths)

    for i, ground_truth in enumerate(l3_ground_truths):
        print(f"  Case {case_counter}: L3 - COUNTERFACTUAL ({ground_truth})")
        case = generate_case("L3", "COUNTERFACTUAL", l3_ground_truth=ground_truth, case_id=case_counter)
        if case and validate_case(case):
            dataset.append(case)
            case_counter += 1
            # Save after each successful case
            with open(output_file, 'w') as f:
                json.dump(dataset, f, indent=2)
            print(f"    ✓ Saved ({len(dataset)} total)")
        else:
            print(f"    ⚠ Failed to generate valid case, retrying...")
            i -= 1

    # Final save (redundant but safe)
    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=2)

    print(f"\n Generated {len(dataset)} cases")
    print(f" Saved to {output_file}")

    # Print statistics
    print("\nDataset Statistics:")
    print(f"  L1: {sum(1 for c in dataset if c['pearl_level'] == 'L1')}")
    print(f"  L2: {sum(1 for c in dataset if c['pearl_level'] == 'L2')}")
    print(f"  L3: {sum(1 for c in dataset if c['pearl_level'] == 'L3')}")

    if any(c.get('ground_truth') for c in dataset):
        print(f"\n  L3 Ground Truth Distribution:")
        print(f"    VALID: {sum(1 for c in dataset if c.get('ground_truth') == 'VALID')}")
        print(f"    INVALID: {sum(1 for c in dataset if c.get('ground_truth') == 'INVALID')}")
        print(f"    CONDITIONAL: {sum(1 for c in dataset if c.get('ground_truth') == 'CONDITIONAL')}")

if __name__ == "__main__":
    generate_dataset()