# T3 Benchmark Extension B - Economics Domain

CS372: Artificial General Intelligence for Reasoning, Planning, and Decision Making
Winter 2026 - Assignment 1

## Overview

This repository contains benchmark cases for the T3 Benchmark Extension B (Economics domain). The goal is to generate **460 cases** testing causal reasoning capabilities across Pearl's Causality Hierarchy.

## Directory Structure

```
assignment_1/
├── analyse.py              # Consolidation and analysis script
├── analysis_report.md      # Generated summary report
├── BenchmarkT3_Extension_B.json  # Consolidated output file
├── atanu/
│   ├── atanu_cases.json    # Atanu's cases
│   ├── atanu_cases.md      # Source markdown
│   └── atanu_to_json.py    # Conversion script
├── chris/
│   ├── chris_cases.json    # Chris's cases
│   ├── chris_cases.md      # Formatted markdown
│   └── chris_to_md.py      # MD generation script
├── mason/
│   ├──  mason_cases.json   # Mason's cases
│   ├──  mason_cases.md     # Mason's cases Markdown
│   └──  md_to_json.py      # Mason's conversion script
└── vivek/
    ├── vivek_cases.json    # Vivek's cases
    ├── vivek_cases.md      # Human-readable markdown format
    ├── json_to_markdown.py # JSON → Markdown converter
    └── markdown_to_json.py # Markdown → JSON parser
```

## JSON Schema Specification

Each case must conform to the following schema:

```json
{
  "id": "T3-BucketLarge-B-{case_id}",
  "bucket": "BucketLarge-B",
  "case_id": "5.xxx",
  "pearl_level": "L1|L2|L3",
  "pearl_level_name": "Association|Intervention|Counterfactual",
  "domain_id": "D5",
  "domain_name": "Economics",
  "scenario": "Observation statement describing what was observed",
  "claim": "Causal conclusion drawn from the observation",
  "label": "YES|NO|MAYBE",
  "label_name": "VALID|FLAWED|CONDITIONAL",
  "is_ambiguous": false,
  "trap": {
    "type": "CONF-MED|REVERSE|SELECTION|COLLIDER|COUNTERFACTUAL|MECHANISM",
    "type_name": "Human readable trap type name",
    "subtype": "Specific_Subtype",
    "subtype_name": "Human readable subtype"
  },
  "variables": {
    "X": { "name": "Treatment/Intervention variable", "role": "intervention|exposure" },
    "Y": { "name": "Outcome variable", "role": "outcome" },
    "Z": [
      { "name": "Confounder/Mediator description", "role": "common_cause|mediator|collider" }
    ],
    "Y0": { "name": "Counterfactual outcome (L3 only)", "role": "counterfactual_outcome" }
  },
  "hidden_structure": {
    "dag_edges": [["Z", "X"], ["Z", "Y"], ["X", "Y"]],
    "notes": "Description of the causal structure",
    "key_insight": "Core insight about why the claim is flawed",
    "hidden_timestamp": "(L2) Temporal ambiguity question",
    "answer_if_tz_lt_tx": "(L2) Answer if Z before X",
    "answer_if_tx_lt_tz": "(L2) Answer if X before Z",
    "counterfactual_query": "(L3) The counterfactual question",
    "ground_truth": "(L3) VALID|INVALID|CONDITIONAL"
  },
  "gold_rationale": "Detailed explanation of why the claim is flawed",
  "ground_truth_reasoning": "(L3) Why this ground truth answer",
  "difficulty": "Easy|Medium|Hard",
  "source": {
    "origin": "generated",
    "file": "source_file.json",
    "generator": "human|llm_generated"
  },
  "annotation": {
    "author": "Author Name",
    "num_annotators": 1,
    "agreement": "generated",
    "adjudicated": true,
    "wise_refusal": "Question identifying missing information needed to evaluate the claim"
  }
}
```

## Field Requirements by Pearl Level

| Field | L1 | L2 | L3 |
|-------|:--:|:--:|:--:|
| scenario | ✓ | ✓ | ✓ |
| claim | ✓ | ✓ | ✓ |
| variables.X | ✓ | ✓ | ✓ |
| variables.Y | ✓ | ✓ | ✓ |
| variables.Z | ✓ | ✓ | ✓ |
| variables.Y0 | - | - | ✓ |
| hidden_structure.dag_edges | ✓ | ✓ | ✓ |
| hidden_structure.hidden_timestamp | - | optional | - |
| hidden_structure.answer_if_tz_lt_tx | - | optional | - |
| hidden_structure.answer_if_tx_lt_tz | - | optional | - |
| hidden_structure.counterfactual_query | - | - | ✓ |
| hidden_structure.ground_truth | - | - | ✓ |
| gold_rationale | ✓ | ✓ | ✓ |
| annotation.wise_refusal | ✓ | ✓ | ✓ |

## Target Distributions

### Pearl Level (460 total)

| Level | Target % | Target Count |
|-------|----------|--------------|
| L1 (Association) | 11% | 51 |
| L2 (Intervention) | 67% | 308 |
| L3 (Counterfactual) | 22% | 101 |

### Difficulty

| Difficulty | Target % | Target Count |
|------------|----------|--------------|
| Easy | 15% | 69 |
| Medium | 59% | 271 |
| Hard | 26% | 120 |

### Trap Types

| Trap Type | Target % | Target Count |
|-----------|----------|--------------|
| CONF-MED | 36% | 166 |
| COUNTERFACTUAL | 22% | 101 |
| REVERSE | 13% | 60 |
| SELECTION | 11% | 51 |
| COLLIDER | 7% | 32 |
| MECHANISM | 2% | 9 |

## Usage

Run the analysis script to consolidate cases and generate the report:

```bash
cd /path/to/assignment_1
python3 analyse.py
```

This will:
1. Load all `[author]_cases.json` files from subdirectories
2. Consolidate into `BenchmarkT3_Extension_B.json`
3. Generate `analysis_report.md` with distribution tables
4. Flag cases with missing mandatory fields

## Report Instructions

```
Here is an example of analysis:
How the pipeline, external tools, and LLM is used:
Coding pipeline and LLM APIs are preferred and allowed, but only as controlled generators + human verification, labelling must be done by human.
Your pasted code or link to your code is needed.
2.   Example of analysis:
(A) Structural sanity check
You should verify and report:
Pearl level distribution (you already did: 11% / 64% / 24%), Maintaining Pearl level distribution approximately
Trap type and subtype coverage: why the previous list is not mutually exclusive or exhaustive, and why you come up with a new list that is mutually exclusive and exhaustive
Presence of ambiguity vs determinate cases
This is dataset analysis, not model evaluation.
(B) Failure-mode analysis (lightweight)
You may:
Run 1–2 representative models
Show qualitative failure patterns
Use this to justify why new cases are needed
Think:
“These 45 cases already expose X, but coverage is sparse / unstable.”
Not:
“Model A beats model B.”
(C) Seed → scale justification
The 45 cases are the canonical seeds.
 Your analysis should motivate:
why they are structurally rich
why they are too small for stable statistics
why controlled expansion is necessary
3.  Other interesting findings from you 
```

## Authors

- Atanu Mukherjee
- Chris Pearce
- Mason Hu
- Vivek Sathe
