from util import *
import re
from tqdm import tqdm
import copy

def add_ids(generated):
    next_id = 3301
    for item in generated:
        for gen in item['generated']:
            gen['annotations']['case_id'] = f"7.{next_id}"
            next_id += 1
    save_json("generated.json", generated)

def find_duplicates(generated):
    trimmed = copy.deepcopy(generated)
    for item in trimmed:
        del item['prompt']
        del item['response']
        for gen in item['generated']:
            if 'similar_cases' in gen:
                del gen['similar_cases']
    save_json("trimmed_generated.json", trimmed)
    prompt_template = """Context: @.CS372_Win2026_Assignment1.pdf
    Take a look at both 'seed' and 'generated' cases in @.trimmed_generated.json.json

    Note any cases that are particularly similar to the following case (besides the case itself).
    Guidelines:
    * Cases with no similarity should not be mentioned.
    * Similar cases must have the same or very similar subdomains.
    * A case is NOT similar just because it shares the same trap type, subdomain, causal structure etc.
    * Differing claims, entity names, specific numbers etc. do not make a case dissimilar on their own.
    * Causal *structure* similarities do NOT on their own make a case similar if the *scenario* described is sufficiently different. In particular, an identical trap type and causal structure example from a completely different subdomain is NOT even "LOW" similarity. For example, falsely attributing a drop in traffic violations and a drop in inmate violence to an interventions at record highs is NOT similar because traffic violations have nothing to do with inmate violence.
    * A case has 'LOW' similarity if there is some overlap in the scenarios, but the reasoning trap is significantly different.
    * A case has 'MEDIUM' similarity if there is some overlap in the scenarios, and the reasoning trap is similar.
    * A case also has 'MEDIUM' similarity if there is significant overlap in the scenarios, but the reasoning trap is significantly different.
    * A case has 'HIGH' similarity if there is significant overlap in the scenario and the reasoning trap is similar. I.e. they are essentially the same case but with different wording/names/numbers/claims etc.

    Case to check:
    ```
    {case}
    ```

    Respond only with JSON in the following format, noting the `case_id` for the similar case, the 'LOW', 'MEDIUM' or 'HIGH' `similarity`, and `explanation` justifies the similarity, for example:
    ```
    [
        {{"case_id": "7.12", "similarity": "HIGH", explanation: "..."}},
        {{"case_id": "7.3356", "similarity": "MEDIUM", explanation: "..."}}
    ]
    """
    for i, item in enumerate(generated):
        print(f"Processing item {i+1}/{len(generated)}")
        for gen in tqdm(item['generated']):
            if 'similar_cases' in gen:
                continue
            prompt = prompt_template.format(case=json.dumps(gen, indent=2))
            response = call_gemini_cli(prompt)
            parsed_response = parse_json(response)
            if parsed_response is not None:
                gen['similar_cases'] = parsed_response
            save_json("generated.json", generated)


if __name__ == "__main__":
    generated = load_json("generated.json")
    add_ids(generated)
    find_duplicates(generated)

