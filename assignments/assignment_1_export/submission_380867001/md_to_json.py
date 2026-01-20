#!/usr/bin/env python3
"""
Convert a Markdown file of Atanu-style "Case" blocks into a JSON dataset matching
the schema of atanu_cases.json.

Usage:
  python md_to_cases_json.py \
    --md "/mnt/data/Untitled document.md" \
    --out "/mnt/data/atanu_cases_from_md.json"
"""

from __future__ import annotations

import argparse
import json
import os
import re
from typing import Any, Dict, List, Optional


PEARL_LEVEL_NAME = {"L1": "Association", "L2": "Intervention", "L3": "Counterfactual"}

TRAP_TYPE_NAME_MAP = {
    "CONF": "Confounding",
    "CONFOUNDING": "Confounding",
    "CONF-MED": "Confounding via Mediator",
    "CONF-MED-COLLIDER": "Confounding via Mediator with Collider",
    "SELECTION": "Selection Bias",
    "SELECTION / COLLIDER": "Selection Bias (Collider)",
    "SELECTION/COLLIDER": "Selection Bias (Collider)",
    "REVERSE": "Reverse Causality",
    "MED": "Mediation Effect",
    "COUNTERFACTUAL": "Counterfactual Reasoning Error",
}


def _clean_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _extract_section(block: str, name: str) -> str:
    """
    Extract content after a header like **Scenario.** up to the next **X.** header,
    next Case heading, or end of block.
    """
    pattern = rf"\*\*{re.escape(name)}\.\*\*\s*(.*?)(?=\n\*\*[^*\n]+?\.\*\*|\n###\s+\*\*Case|\Z)"
    m = re.search(pattern, block, flags=re.S)
    return m.group(1).strip() if m else ""


def _parse_bullets_as_kv(text: str) -> Dict[str, str]:
    """
    Parse lines like:
      • Case ID: 7.95
    into {"Case ID": "7.95"}.
    """
    out: Dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"[•\-\*]\s*([^:]+):\s*(.*)", line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def _parse_variables(text: str) -> Dict[str, str]:
    """
    Parse lines like:
      • X \= Something
    into {"X": "Something"}.
    """
    out: Dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"[•\-\*]\s*([A-Za-z0-9′]+)\s*\\?=\s*(.*)", line)
        if m:
            out[m.group(1)] = _clean_ws(m.group(2))
    return out


def _parse_dag_edges(causal_structure: str) -> List[List[str]]:
    """
    Parse a 'Causal Structure' string into a list of [src, dst] edges.
    Supports arrows '→' and '->'. Ignores purely disjunctive prose fragments.
    """
    if not causal_structure:
        return []
    cs = causal_structure.replace("→", "->")

    edges: List[List[str]] = []
    # Split on commas/semicolons to reduce noise
    for chunk in re.split(r"[;,]\s*", cs):
        chunk = chunk.strip()
        if not chunk:
            continue
        for a, b in re.findall(r"([A-Za-z0-9]+)\s*-\>\s*([A-Za-z0-9]+)", chunk):
            edges.append([a, b])
    return edges


def _extract_claim_from_scenario(scenario: str) -> str:
    """
    Heuristic: use the last curly-quoted string as the explicit causal claim,
    else fall back to the last sentence fragment.
    """
    quotes = re.findall(r"“([^”]+)”", scenario)
    if quotes:
        return quotes[-1].strip()
    # fallback: last sentence-ish
    parts = [p.strip() for p in scenario.split(".") if p.strip()]
    return parts[-1] if parts else ""


def _merge_wrapped_conditional_lines(lines: List[str]) -> List[str]:
    """
    Markdown often hard-wraps; merge lines that belong to the previous conditional.
    """
    merged: List[str] = []
    for line in lines:
        if re.match(r"^(Answer if|If)\s+t", line):
            merged.append(line)
        elif merged:
            merged[-1] += " " + line
        else:
            merged.append(line)
    return merged


def _parse_conditional_answers(text: str) -> Dict[str, str]:
    """
    Extract branches like:
      Answer if tZ < tX .....
      Answer if tX < tZ .....
    Returns dict with optional keys:
      answer_if_tz_lt_tx
      answer_if_tx_lt_tz
    """
    out: Dict[str, str] = {}
    if not text:
        return out

    lines = [l.strip() for l in text.splitlines() if l.strip()]
    lines = _merge_wrapped_conditional_lines(lines)

    for line in lines:
        m = re.match(r"^(?:Answer if|If)\s+(t[^ ]+)\s*\\?<\s*(t[^ ]+)", line)
        if not m:
            continue

        left, right = m.group(1), m.group(2)
        # take text after first period if present (keeps it cleaner)
        body = line.split(".", 1)[1].strip() if "." in line else line.strip()

        if left.startswith("tX") and not right.startswith("tX"):
            out["answer_if_tx_lt_tz"] = body
        elif right.startswith("tX") and not left.startswith("tX"):
            out["answer_if_tz_lt_tx"] = body

    return out


def parse_markdown_cases(md_text: str, md_filename: str) -> List[Dict[str, Any]]:
    """
    Main parser: split into Case blocks and create JSON objects.
    """
    blocks = re.split(r"\n(?=###\s+\*\*Case\s+)", md_text)
    cases: List[Dict[str, Any]] = []

    for block in blocks:
        block = block.strip()
        if not block.startswith("###"):
            continue

        head = re.search(r"###\s+\*\*Case\s+([0-9.]+):\s*(.*?)\*\*", block)
        if not head:
            continue
        case_id = head.group(1).strip()
        _title = head.group(2).strip()  # not used in the output schema, but kept here if you want it later

        scenario = _extract_section(block, "Scenario")
        variables_raw = _extract_section(block, "Variables")
        annotations_raw = _extract_section(block, "Annotations")
        hidden_ts = _extract_section(block, "Hidden Timestamp")
        conditional_answers_raw = _extract_section(block, "Conditional Answers")
        wise_refusal = _extract_section(block, "Wise Refusal")

        var_map = _parse_variables(variables_raw)
        ann = _parse_bullets_as_kv(annotations_raw)

        pearl_level_text = ann.get("Pearl Level", "")
        pearl_level_match = re.search(r"(L[123])", pearl_level_text)
        pearl_level = pearl_level_match.group(1) if pearl_level_match else ""

        domain_text = ann.get("Domain", "Economics")
        domain_name = domain_text.split("(")[0].strip() or "Economics"

        trap_type = ann.get("Trap Type", "").strip()
        trap_subtype = ann.get("Trap Subtype", "").strip()

        difficulty = ann.get("Difficulty", "").strip() or None
        causal_structure = ann.get("Causal Structure", "").strip()
        key_insight = ann.get("Key Insight", "").strip()

        claim = _extract_claim_from_scenario(scenario)

        dag_edges = _parse_dag_edges(causal_structure)
        cond = _parse_conditional_answers(conditional_answers_raw)

        # Variable roles (heuristic)
        x_role = "intervention" if pearl_level in ("L2", "L3") else "exposure"
        variables_obj: Dict[str, Any] = {
            "X": {"name": var_map.get("X", ""), "role": x_role},
            "Y": {"name": var_map.get("Y", ""), "role": "outcome"},
            "Z": [],
            "Y0": None,
        }

        if "Y0" in var_map or "Y′" in var_map:
            y0_name = var_map.get("Y0") or var_map.get("Y′")
            variables_obj["Y0"] = {"name": y0_name, "role": "counterfactual_outcome"}

        # Put everything except X/Y/Y0 into Z list
        t_upper = trap_type.upper()
        for k, name in var_map.items():
            if k in ("X", "Y", "Y0", "Y′"):
                continue

            role = "common_cause"
            if ("MED" in t_upper and k.startswith("M")) or ("mediator" in name.lower()):
                role = "mediator"
            if ("SELECTION" in t_upper or "COLLIDER" in t_upper) and (
                k in ("S", "K") or "selection" in name.lower() or "collider" in name.lower()
            ):
                role = "collider"

            variables_obj["Z"].append({"name": name, "role": role})

        # Trap type_name
        trap_key = trap_type.strip()
        trap_key_norm = trap_key.replace("CONFOUNDING", "CONF")
        type_name = TRAP_TYPE_NAME_MAP.get(trap_key) or TRAP_TYPE_NAME_MAP.get(trap_key_norm) or trap_key.title()

        # Labels: follow the provided JSON convention where L3/counterfactuals are conditional
        if pearl_level == "L3" or "COUNTERFACTUAL" in t_upper:
            label, label_name, is_ambiguous = "MAYBE", "CONDITIONAL", True
        else:
            label, label_name, is_ambiguous = "NO", "FLAWED", False

        case_obj: Dict[str, Any] = {
            "id": f"T3-BucketLarge-B-{case_id}",
            "bucket": "BucketLarge-B",
            "case_id": case_id,
            "pearl_level": pearl_level,
            "pearl_level_name": PEARL_LEVEL_NAME.get(pearl_level, ""),
            "domain_id": "D5",
            "domain_name": domain_name,
            "scenario": _clean_ws(scenario),
            "claim": claim,
            "label": label,
            "label_name": label_name,
            "is_ambiguous": is_ambiguous,
            "trap": {
                "type": trap_type,
                "type_name": type_name,
                "subtype": trap_subtype,
                "subtype_name": trap_subtype.title() if trap_subtype else "",
            },
            "variables": variables_obj,
            "hidden_structure": {
                "dag_edges": dag_edges,
                "notes": causal_structure,
                "key_insight": key_insight,
                "hidden_timestamp": hidden_ts,
                **cond,
            },
            "gold_rationale": key_insight,
            "difficulty": difficulty,
            "source": {"origin": "generated", "file": md_filename, "generator": "llm_generated"},
            "annotation": {
                "author": "Atanu Mukherjee",
                "num_annotators": 1,
                "agreement": "generated",
                "adjudicated": True,
                "wise_refusal": wise_refusal.strip("“”"),
            },
        }

        cases.append(case_obj)

    return cases


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True, help="Path to the input Markdown file")
    ap.add_argument("--out", required=True, help="Path to write the output JSON file")
    args = ap.parse_args()

    with open(args.md, "r", encoding="utf-8") as f:
        md_text = f.read()

    cases = parse_markdown_cases(md_text, md_filename=os.path.basename(args.md))

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(cases)} cases to {args.out}")


if __name__ == "__main__":
    main()
