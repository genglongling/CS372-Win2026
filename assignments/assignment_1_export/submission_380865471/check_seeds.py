import json
import subprocess
from util import *

def get_pass_fail(response):
    if "<verdict>PASS</verdict>" in response:
        return "PASS"
    elif "<verdict>FAIL</verdict>" in response:
        return "FAIL"
    else:
        return None

if __name__ == "__main__":
    seeds = load_json("seeds.json")
    print("Seeds length:", len(seeds))
    seeds_by_id = {seed['annotations']['case_id']: seed for seed in seeds}
    ids = set(seeds_by_id.keys())
    print("Unique ids:", len(ids))
    subdomains = set([seed['annotations']['subdomain'] for seed in seeds])
    print("Unique subdomains:", len(subdomains))
    for subdomain in subdomains:
        print(subdomain)

    traps = set([seed['annotations']['trap_type'] for seed in seeds])
    print()
    print("Unique traps:", len(traps))
    for trap in traps:
        print(trap)

    subtraps = set([seed['annotations']['trap_subtype'] for seed in seeds])
    print()
    print("Unique subtraps:", len(subtraps))
    for subtrap in subtraps:
        print(subtrap)

    sentence_counts = [len(seed['scenario'].split('. ')) for seed in seeds]
    print("Max sentences in scenario:", max(sentence_counts))
    print("Mean sentences in scenario:", sum(sentence_counts)/len(sentence_counts))

    check_prompt = """The following JSON was extracted from @.BenchmarkT3-BucketLarge-C.pdf
    Verify that all the information in the JSON is contained in the PDF, and all information in the PDF is contained in the JSON.
    Note any discrepancies between the two beyond minor formatting issues.
    Conclude with either "<verdict>PASS</verdict>" if there are no discrephancies or "<verdict>FAIL</verdict>" if there are.  
    Here is the JSON:
    ```
    {case_json}
    ```
    """

    checked_seeds = load_json("check_seeds.json")
    checked_ids = set([checked['case_id'] for checked in checked_seeds])
    remaining_to_check = ids - checked_ids
    print("Remaining to check:", len(remaining_to_check))
    # remaining_to_check = list(remaining_to_check)[:6]  # Limit to first 6 for testing
    for case_id in remaining_to_check:
        seed = seeds_by_id[case_id]
        prompt = check_prompt.format(case_json=json.dumps(seed, indent=2))
        response = call_gemini_cli(prompt)
        if response is None:
            print("Skipping case_id due to CLI error:", case_id)
            continue
        passfail = get_pass_fail(response)
        if passfail is None:
            print("Could not determine PASS/FAIL for case_id:", case_id)
            print("Response:", response)
            continue
        checked_seeds.append({
            "case_id": case_id,
            "passfail": passfail,
            "prompt": prompt,
            "response": response
        })
    save_json("check_seeds.json", checked_seeds)