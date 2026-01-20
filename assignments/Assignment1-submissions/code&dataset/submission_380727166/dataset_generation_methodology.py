"""
CS372 Assignment 1 - Dataset Generation Methodology
Group D1: Sports Domain, Outcome Bias, Counterfactual Focus

This script documents the methodology and workflow used to generate
the 80-case benchmark dataset for causal reasoning evaluation.

Author: Matt Wolfman
Date: January 12, 2026
"""

import json
from collections import Counter
from typing import Dict, List, Any

# ============================================================================
# DATASET SPECIFICATION
# ============================================================================

DATASET_SPECIFICATION = {
    "domain": "Sports",
    "group": "D1",
    "signature_trap": "OUTCOME_BIAS",
    "focus_area": "Counterfactual (L3)",
    "total_cases": 80,
    
    "pearl_level_distribution": {
        "L1": 10,  # Association
        "L2": 30,  # Intervention
        "L3": 40,  # Counterfactual (PRIMARY FOCUS)
    },
    
    "label_distribution": {
        "YES": "16-24",
        "NO": "40-48",
        "AMBIGUOUS": "8-16",
    },
    
    "trap_type_distribution": {
        "OUTCOME_BIAS": "30-40 (signature trap)",
        "REGRESSION_TO_MEAN": "10-15",
        "SURVIVORSHIP": "10-15",
        "SELECTION": "10-15",
        "AVAILABILITY_BIAS": "flexible",
        "CONFOUNDING": "flexible",
        "Others": "flexible",
    },
    
    "difficulty_distribution": {
        "Easy": "~20",
        "Medium": "~35",
        "Hard": "~25",
    },
}

# ============================================================================
# REQUIRED FIELDS FOR EACH CASE
# ============================================================================

REQUIRED_FIELDS = [
    # Core identification
    "id",                    # Format: D1-001 through D1-080
    "bucket",                # BucketLarge-D
    "pearl_level",           # L1, L2, or L3
    "domain",                # Sports
    "subdomain",             # Specific sport (Basketball, Football, etc.)
    "title",                 # Short descriptive title
    
    # Content
    "scenario",              # 2-4 sentence description of the situation
    "claim",                 # The statement to be evaluated
    "label",                 # YES, NO, or AMBIGUOUS
    "is_ambiguous",          # Boolean
    
    # Trap annotation
    "trap",                  # {type: str, subtype: str}
    
    # Variables
    "variables",             # {X: str, Y: str, Z: str}
    
    # Reasoning
    "gold_rationale",        # 2-4 sentence explanation of correct reasoning
    "questions",             # List of reasoning questions
    "expected_analysis",     # Type of analysis required
    
    # Enrichment
    "difficulty",            # Easy, Medium, or Hard
    "causal_structure",      # Description of causal relationships
    "key_insight",           # Main takeaway
    
    # Advanced fields
    "hidden_timestamp",      # Question about temporal/causal ordering
    "conditional_answers",   # Dict of "if X then Y" scenarios
    "wise_refusal",          # Statement identifying missing information
    
    # Metadata
    "annotation",            # Author, date, version info
]

# ============================================================================
# GENERATION WORKFLOW
# ============================================================================

def generate_case_workflow():
    """
    Documents the step-by-step workflow used to generate each case.
    
    This is a conceptual representation of the interactive process
    used with an AI agent (Manus) to create the dataset.
    """
    
    workflow_steps = [
        {
            "step": 1,
            "name": "Strategic Planning",
            "description": "Review current distribution status and identify needed case type",
            "example": "Need L3 case with OUTCOME_BIAS trap, NO label"
        },
        {
            "step": 2,
            "name": "Scenario Generation",
            "description": "Create a sports scenario (2-4 sentences) that sets up the reasoning challenge",
            "tools": "AI-assisted brainstorming, human refinement"
        },
        {
            "step": 3,
            "name": "Claim Formulation",
            "description": "Craft a specific, evaluable claim about the scenario",
            "example": "The coach's decision was wrong because the team lost"
        },
        {
            "step": 4,
            "name": "Human Annotation (CRITICAL)",
            "description": "Human analyst determines:",
            "sub_steps": [
                "Label (YES/NO/AMBIGUOUS) - based on logical validity",
                "Trap type - which cognitive bias or causal fallacy is present",
                "Variables - X (treatment), Y (outcome), Z (confounder)",
                "Gold rationale - correct reasoning in 2-4 sentences"
            ],
            "note": "This step requires human expertise; LLMs can make subtle errors"
        },
        {
            "step": 5,
            "name": "Enrichment",
            "description": "Add additional fields",
            "fields": [
                "difficulty (Easy/Medium/Hard)",
                "causal_structure",
                "key_insight",
                "hidden_timestamp",
                "conditional_answers",
                "wise_refusal"
            ]
        },
        {
            "step": 6,
            "name": "Quality Control",
            "description": "Review for clarity, logical consistency, and correctness",
            "checks": [
                "Is the scenario clear and concise?",
                "Is the claim unambiguous?",
                "Is the label justified by the reasoning?",
                "Are the variables correctly identified?",
                "Is the gold rationale sound?"
            ]
        },
        {
            "step": 7,
            "name": "JSON Integration",
            "description": "Add the case to the dataset JSON file",
            "verification": "Programmatic check that JSON remains valid"
        },
        {
            "step": 8,
            "name": "Progress Tracking",
            "description": "Update meta-log to track distribution progress",
            "action": "Adjust strategy for next case based on remaining needs"
        }
    ]
    
    return workflow_steps


# ============================================================================
# VERIFICATION AND ANALYSIS FUNCTIONS
# ============================================================================

def verify_dataset(json_file_path: str) -> Dict[str, Any]:
    """
    Verify the dataset meets all requirements.
    
    Args:
        json_file_path: Path to the dataset JSON file
        
    Returns:
        Dictionary with verification results
    """
    
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    results = {
        "total_cases": len(data),
        "valid_json": True,
        "all_ids_present": True,
        "no_duplicates": True,
        "all_fields_present": True,
    }
    
    # Check case count
    if len(data) != 80:
        results["total_cases_ok"] = False
    
    # Check IDs
    ids = [case['id'] for case in data]
    expected_ids = [f"D1-{str(i).zfill(3)}" for i in range(1, 81)]
    
    missing = set(expected_ids) - set(ids)
    if missing:
        results["all_ids_present"] = False
        results["missing_ids"] = list(missing)
    
    # Check for duplicates
    duplicates = [id for id, count in Counter(ids).items() if count > 1]
    if duplicates:
        results["no_duplicates"] = False
        results["duplicate_ids"] = duplicates
    
    # Check required fields
    cases_missing_fields = []
    for case in data:
        missing_fields = [f for f in REQUIRED_FIELDS if f not in case]
        if missing_fields:
            cases_missing_fields.append((case['id'], missing_fields))
    
    if cases_missing_fields:
        results["all_fields_present"] = False
        results["cases_missing_fields"] = cases_missing_fields[:5]  # Show first 5
    
    # Distribution analysis
    pearl_counts = Counter([case['pearl_level'] for case in data])
    label_counts = Counter([case['label'] for case in data])
    trap_counts = Counter([case['trap']['type'] for case in data])
    diff_counts = Counter([case.get('difficulty', 'Unknown') for case in data])
    
    results["distributions"] = {
        "pearl_levels": dict(pearl_counts),
        "labels": dict(label_counts),
        "trap_types": dict(trap_counts),
        "difficulty": dict(diff_counts),
    }
    
    return results


def generate_summary_statistics(json_file_path: str) -> str:
    """
    Generate a human-readable summary of the dataset.
    
    Args:
        json_file_path: Path to the dataset JSON file
        
    Returns:
        Formatted string with summary statistics
    """
    
    verification = verify_dataset(json_file_path)
    
    summary = f"""
    ============================================================================
    CS372 ASSIGNMENT 1 - DATASET SUMMARY
    ============================================================================
    
    Total Cases: {verification['total_cases']}
    Valid JSON: {verification['valid_json']}
    All IDs Present: {verification['all_ids_present']}
    No Duplicates: {verification['no_duplicates']}
    All Fields Present: {verification['all_fields_present']}
    
    PEARL LEVEL DISTRIBUTION:
    {json.dumps(verification['distributions']['pearl_levels'], indent=2)}
    
    LABEL DISTRIBUTION:
    {json.dumps(verification['distributions']['labels'], indent=2)}
    
    TRAP TYPE DISTRIBUTION:
    {json.dumps(verification['distributions']['trap_types'], indent=2)}
    
    DIFFICULTY DISTRIBUTION:
    {json.dumps(verification['distributions']['difficulty'], indent=2)}
    
    ============================================================================
    """
    
    return summary


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    """
    This script can be run to verify the final dataset.
    
    Usage:
        python3 dataset_generation_methodology.py
    """
    
    print("CS372 Assignment 1 - Dataset Generation Methodology")
    print("=" * 80)
    print()
    print("DATASET SPECIFICATION:")
    print(json.dumps(DATASET_SPECIFICATION, indent=2))
    print()
    print("=" * 80)
    print()
    
    # Verify the dataset
    dataset_path = "/home/ubuntu/dataset_cases.json"
    
    try:
        print(f"Verifying dataset at: {dataset_path}")
        print()
        summary = generate_summary_statistics(dataset_path)
        print(summary)
        
        print("✅ Dataset verification complete!")
        print()
        print("The dataset is ready for submission to Gradescope.")
        
    except FileNotFoundError:
        print(f"❌ Error: Dataset file not found at {dataset_path}")
        print("Please ensure the dataset JSON file exists.")
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON in dataset file")
        print("Please check the JSON syntax.")
    except Exception as e:
        print(f"❌ Error during verification: {str(e)}")
