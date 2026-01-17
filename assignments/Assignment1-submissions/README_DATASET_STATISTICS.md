# Assignment 1 Dataset Statistics Summary

This document provides a comprehensive summary of the dataset statistics for each group (A-J) in Assignment 1. For each group, there are two rows:
1. **With authors**: Cases that have author fields matching enrolled students
2. **No author**: Cases without author fields or with authors that don't match enrolled students

## Dataset Statistics by Group

| Group | Number | Fields | Pearl Distribution | Label Distribution | Authors |
|-------|--------|--------|---------------------|---------------------|---------|
| A (with authors) | 230 | 23 fields<br/>(LLM, author, bucket, case_id, causal_structure, conditional_answers, correct_reasoning, difficulty_level, ...) | L1: 10.9% (25)<br/>L2: 67.0% (154)<br/>L3: 22.2% (51) | L1: Y=0% N=100% A=0%<br/>L2: Y=0% N=100% A=0%<br/>L3: Y=0% N=100% A=0% | 1 authors<br/>(Daphne) |
| A (no author) | 116 | 23 fields<br/>(LLM, author, bucket, case_id, causal_structure, conditional_answers, correct_reasoning, difficulty_level, ...) | L1: 15.8% (12)<br/>L2: 57.9% (44)<br/>L3: 26.3% (20) | L1: Y=0% N=100% A=0%<br/>L2: Y=0% N=100% A=0%<br/>L3: Y=0% N=100% A=0% | Author field:<br/>(Rebecca, no author field) |
| B (with authors) | 930 | 23 fields<br/>(_causal_structure, annotation, bucket, case_id, claim, difficulty, domain_id, domain_name, ...) | L1: 9.7% (90)<br/>L2: 70.8% (658)<br/>L3: 19.6% (182) | L1: Y=0% N=100% A=0%<br/>L2: Y=0% N=100% A=0%<br/>L3: Y=8% N=42% A=51% | 4 authors<br/>(Atanu Mukherjee, Chris Pearce, Mason Hu, Vivek Sathe) |
| C (with authors) | 191 | 30 fields<br/>(annotation, annotations, bucket, claim, conditional_answers, correct_reasoning, domain, evidence_of_pretext, ...) | L1: 11.0% (21)<br/>L2: 69.6% (133)<br/>L3: 19.4% (37) | L1: Y=48% N=10% A=43%<br/>L2: Y=30% N=41% A=29%<br/>L3: Y=35% N=30% A=35% | 2 authors<br/>(Andy Ouyang, mhayes3) |
| C (no author) | 50 | 30 fields<br/>(annotation, annotations, bucket, claim, conditional_answers, correct_reasoning, domain, evidence_of_pretext, ...) | L1: 10.0% (5)<br/>L2: 70.0% (35)<br/>L3: 20.0% (10) | L3: Y=40% N=20% A=40% | Author field:<br/>(no author field) |
| D (with authors) | 241 | 27 fields<br/>(annotation, annotations, bucket, case_id, causal_structure, claim, conditional_answer, conditional_answers, ...) | L1: 19.9% (48)<br/>L2: 42.7% (103)<br/>L3: 37.3% (90) | L1: Y=4% N=88% A=8%<br/>L2: Y=5% N=82% A=14%<br/>L3: Y=34% N=47% A=19% | 3 authors<br/>(Matt Wolfman, Samantha van Rijs, Yuqiao Zeng) |
| D (no author) | 78 | 27 fields<br/>(annotation, annotations, bucket, case_id, causal_structure, claim, conditional_answer, conditional_answers, ...) | L1: 12.8% (10)<br/>L2: 65.4% (51)<br/>L3: 21.8% (17) | N/A | Author field:<br/>(no author field) |
| E (no author) | 355 | 25 fields<br/>(annotation, bucket, case_id, causal_structure, claim, conditional_answers, difficulty, domain_id, ...) | L1: 13.5% (48)<br/>L2: 64.5% (229)<br/>L3: 22.0% (78) | L1: Y=38% N=44% A=19%<br/>L2: Y=31% N=46% A=23%<br/>L3: Y=26% N=26% A=49% | Author field:<br/>(no author field) |
| F (with authors) | 310 | 21 fields<br/>(annotation, bucket, case_id, claim, difficulty, domain, expected_reasoning, gold_rationale, ...) | L1: 11.6% (36)<br/>L2: 69.4% (215)<br/>L3: 19.0% (59) | L1: Y=0% N=72% A=28%<br/>L2: Y=10% N=36% A=54%<br/>L3: Y=24% N=34% A=42% | 3 authors<br/>(April Yang, Mingyang, Sameer Vijay) |
| G (with authors) | 742 | 26 fields<br/>(annotations, causalStructure, claim, compilerOptions, conditionalAnswers, difficulty, domain, exclude, ...) | L1: 21.0% (156)<br/>L2: 48.8% (362)<br/>L3: 30.2% (224) | L1: Y=31% N=47% A=22%<br/>L2: Y=31% N=52% A=17%<br/>L3: Y=14% N=54% A=31% | 3 authors<br/>(deveen, lgren007, wutheodo) |
| G (no author) | 177 | 26 fields<br/>(annotations, causalStructure, claim, compilerOptions, conditionalAnswers, difficulty, domain, exclude, ...) | L1: 15.0% (24)<br/>L2: 66.2% (106)<br/>L3: 18.8% (30) | L1: Y=17% N=75% A=8%<br/>L2: Y=43% N=49% A=8%<br/>L3: Y=33% N=60% A=7% | Author field:<br/>(LLM, no author field) |
| H (with authors) | 133 | 19 fields<br/>(annotation, bucket, causal_structure, claim, conditional_answers, difficulty, domain, gold_rationale, ...) | L1: 27.8% (37)<br/>L2: 72.2% (96)<br/>L3: 0.0% (0) | L1: Y=0% N=100% A=0%<br/>L2: Y=0% N=100% A=0% | 1 authors<br/>(Veljko Skarich) |
| I (with authors) | 80 | 25 fields<br/>(annotation, annotations, bucket, case_id, causal_structure, claim, conditional_answers, correct_reasoning, ...) | L1: 12.5% (10)<br/>L2: 62.5% (50)<br/>L3: 25.0% (20) | L1: Y=0% N=100% A=0%<br/>L2: Y=0% N=100% A=0%<br/>L3: Y=40% N=60% A=0% | 1 authors<br/>(Alanood) |
| I (no author) | 454 | 25 fields<br/>(annotation, annotations, bucket, case_id, causal_structure, claim, conditional_answers, correct_reasoning, ...) | L1: 11.5% (52)<br/>L2: 61.0% (277)<br/>L3: 27.5% (125) | N/A | Author field:<br/>(no author field) |
| J (with authors) | 710 | 27 fields<br/>(Conditional Answers, Hidden Timestamp, Wise Refusal, annotation, annotations, bucket, case_id, causal_structure, claim, ...) | L1: 11.3% (26)<br/>L2: 67.0% (154)<br/>L3: 21.7% (50) | L1: Y=0% N=88% A=12%<br/>L2: Y=10% N=88% A=2%<br/>L3: Y=0% N=62% A=38% | 2 authors<br/>(Kelvin Christian, Sreya Vangara) |
| **Total** | **4,797**<br/>(3,567 with authors, 1,230 no author) | - | L1: 14.1% (600)<br/>L2: 62.6% (2,667)<br/>L3: 23.3% (993) | L1: Y=15% N=71% A=13%<br/>L2: Y=13% N=74% A=13%<br/>L3: Y=17% N=50% A=33% | - |

## Column Descriptions

- **Group**: Group identifier (A-J) with indication of whether cases have student authors or not
- **Number**: Total number of cases in that category
- **Fields**: Number and list of unique top-level fields found in the dataset cases
- **Pearl Distribution**: Distribution of cases across Pearl Levels (L1: Association, L2: Intervention, L3: Counterfactual) with percentages and counts
- **Label Distribution**: Distribution of labels (Y=YES, N=NO, A=AMBIGUOUS) across each Pearl Level, showing the percentage breakdown
- **Authors**: For "with authors" rows: Number of unique student authors and their identifiers (email local parts or names). For "no author" rows: Author field values found (e.g., "LLM", "no author field", or non-matching author names)

## Notes

- **With authors**: Cases where the author field matches an enrolled student in that group (based on email or name matching)
- **No author**: Cases without author fields, cases with "LLM" as author, or cases where the author doesn't match any enrolled student
- Group E shows only "no author" cases, indicating that submitted files don't have matching author fields for enrolled students
- Pearl Level distributions are calculated separately for cases with and without student authors
- Label distributions show the ratio of YES/NO/AMBIGUOUS labels within each Pearl Level
- Field counts include top-level fields only; nested fields (e.g., `annotations.author`) are not counted separately
- Some groups may have significantly more cases without student authors, which could indicate missing author attribution or cases generated by non-student sources

## Generation

This table is generated automatically from the submission analysis. To regenerate, run:

```bash
python3 generate_dataset_summary.py
```
