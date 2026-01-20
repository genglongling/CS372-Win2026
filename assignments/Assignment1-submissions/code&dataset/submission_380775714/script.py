import json
import os
from openai import OpenAI

# ==========================================
# CONFIGURATION
# ==========================================
# Replace with your actual API key
API_KEY = "YOUR_OPENAI_API_KEY" 
client = OpenAI(api_key=API_KEY)

INPUT_FILE = 'json_data.json'      # Your existing seed file
OUTPUT_FILE = 'expanded_dataset.json'

# ==========================================
# PROMPT TEMPLATES (The "Clear Prompts")
# ==========================================

# STEP 1 PROMPT: Controlled Generation
GEN_SYSTEM_PROMPT = """
You are an expert in Pearl's Causality Hierarchy and Causal Reasoning Benchmarks. 
Your task is to generate new 'Daily Life' reasoning cases based on a provided seed case.

For the given seed, generate 3 new variations:
1. VARIATION A (Same Trap, Different Context): Keep the same causal trap/fallacy but change the scenario domain (e.g., from Health to Workplace).
2. VARIATION B (Different Pearl Level): Change the Pearl Level (Association vs Intervention vs Counterfactual).
3. VARIATION C (Valid/Control Case): A scenario with similar variables where the reasoning is CORRECT (Label: YES).

Output strictly valid JSON list of objects. Each object must have:
- scenario: A short description.
- claim: The causal claim being made.
- variables: {X, Y, Z} definitions.
- hidden_structure: The true causal structure (DAG).
- trap: {type, subtype} (if applicable, else "None").
- pearl_level: L1, L2, or L3.
- label: NO (flawed), YES (valid), or CONDITIONAL.
- wise_refusal: A sentence explaining why we can't be sure (for NO/CONDITIONAL).
"""

# STEP 3 PROMPT: Initial Labeling (Auto-Annotation)
LABEL_SYSTEM_PROMPT = """
You are an expert Annotator for the T3 Causal Benchmark.
Analyze the provided case and assign the following metadata based on strict definitions:

1. pearl_level: 
   - L1 (Association): Observational only.
   - L2 (Intervention): Involves action/policy change.
   - L3 (Counterfactual): "What would have happened if..."
2. trap: Identify the specific fallacy (e.g., Confounding, Selection Bias, Regression to Mean).
3. label: 
   - NO: The claim is flawed.
   - YES: The claim is valid.
   - CONDITIONAL: True only under specific unstated assumptions.

Return the result as a JSON object merging the input case with these new fields.
"""

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def call_llm(system_prompt, user_content):
    """
    Generic wrapper to call the LLM. 
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Or gpt-4-turbo
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"LLM Call Failed: {e}")
        return None

def validate_case_structure(case):
    """
    Step 2: Structural Validation Check
    Ensures all required fields from the spec are present.
    """
    required_fields = [
        "scenario", "claim", "variables", "pearl_level", 
        "label", "trap", "wise_refusal"
    ]
    missing = [f for f in required_fields if f not in case]
    
    if missing:
        print(f"  [!] Validation Failed. Missing keys: {missing}")
        return False
    return True

# ==========================================
# PIPELINE STEPS
# ==========================================

def step_1_generation(seed_cases):
    print(f"\n--- STEP 1: GENERATION (Looping through {len(seed_cases)} seeds) ---")
    new_cases = []
    
    # For demo purposes, we loop through the first 2 seeds. 
    # In production, remove [:2] to process all.
    for i, seed in enumerate(seed_cases[:2]): 
        print(f"Generating variations for Seed ID: {seed.get('id', i)}...")
        
        user_content = json.dumps(seed)
        
        # CALL LLM
        response_text = call_llm(GEN_SYSTEM_PROMPT, f"Seed Case:\n{user_content}")
        
        if response_text:
            try:
                # Parse the JSON list returned by LLM
                generated_list = json.loads(response_text)
                
                # Unwrap if the LLM put it inside a dictionary key like "cases"
                if isinstance(generated_list, dict):
                    generated_list = generated_list.get("cases", generated_list.get("variations", []))
                
                print(f"  -> Generated {len(generated_list)} raw variations.")
                new_cases.extend(generated_list)
                
            except json.JSONDecodeError:
                print("  [!] Failed to parse LLM JSON response.")
    
    return new_cases

def step_2_validation(raw_cases):
    print(f"\n--- STEP 2: STRUCTURAL VALIDATION ---")
    valid_cases = []
    for idx, case in enumerate(raw_cases):
        if validate_case_structure(case):
            # Assign a temp ID
            case['id'] = f"gen_draft_{idx}"
            valid_cases.append(case)
    
    print(f"Validation complete. {len(valid_cases)}/{len(raw_cases)} cases passed.")
    return valid_cases

def step_3_labeling(valid_cases):
    print(f"\n--- STEP 3: INITIAL LABELING (Bootstrapping) ---")
    labeled_cases = []
    
    for case in valid_cases:
        print(f"Labeling case: {case['id']}...")
        
        # We strip existing labels to force the LLM to think from scratch (Verification)
        clean_case = {k: v for k, v in case.items() if k not in ['pearl_level', 'trap', 'label']}
        
        user_content = json.dumps(clean_case)
        
        # CALL LLM
        response_text = call_llm(LABEL_SYSTEM_PROMPT, f"Classify this case:\n{user_content}")
        
        if response_text:
            try:
                annotations = json.loads(response_text)
                # Merge AI annotations back into the case
                case.update(annotations)
                labeled_cases.append(case)
            except json.JSONDecodeError:
                print("  [!] Failed to parse annotation JSON.")
    
    return labeled_cases

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # 0. Load Seeds
    try:
        with open(INPUT_FILE, 'r') as f:
            seeds = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        seeds = []

    if seeds:
        # Run Pipeline
        generated_raw = step_1_generation(seeds)
        validated_data = step_2_validation(generated_raw)
        final_data = step_3_labeling(validated_data)
        
        # Save Output
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(final_data, f, indent=2)
            
        print(f"\nSUCCESS: Pipeline finished. Saved {len(final_data)} cases to {OUTPUT_FILE}")
        print("Next Step: Human Verification (Manual Review)")