import json
import numpy as np
from collections import Counter
import os

files = os.listdir(".")

dataset = []
for fn in files:
    if fn.endswith("author.json"):
        with open(fn, "r") as f:
            dataset.extend(json.load(f))


total_examples = len(dataset)

domains = [ex['annotations']['Domain'] for ex in dataset]
trap_types = [ex['annotations']['Trap Type'] for ex in dataset]
pearl_levels = [ex['annotations']['Pearl Level'] for ex in dataset]
difficulties = [ex['annotations']['Difficulty'] for ex in dataset]
subdomains = [ex['annotations']['Subdomain'] for ex in dataset]

# Counts
domain_counts = Counter(domains)
trap_counts = Counter(trap_types)
pearl_counts = Counter(pearl_levels)
difficulty_counts = Counter(difficulties)
subdomain_counts = Counter(subdomains)

# Text stats
scenario_lengths = [len(ex['scenario'].split()) for ex in dataset]
title_lengths = [len(ex['title'].split()) for ex in dataset]
questions_lengths = [len(ex['questions'].split()) for ex in dataset]

# Variables
num_variables = [len(ex['variables']) for ex in dataset]

# Wise refusal presence
wise_refusal_count = sum(1 for ex in dataset if ex.get('Wise Refusal'))

# Output summary
summary = {
    'total_examples': total_examples,
    'domain_counts': domain_counts,
    'trap_counts': trap_counts,
    'pearl_counts': pearl_counts,
    'difficulty_counts': difficulty_counts,
    'subdomain_counts': subdomain_counts,
    'avg_scenario_length': np.mean(scenario_lengths),
    'avg_title_length': np.mean(title_lengths),
    'avg_questions_length': np.mean(questions_lengths),
    'avg_num_variables': np.mean(num_variables),
    'wise_refusal_count': wise_refusal_count
}

print(summary)

with open("GroupJ1_dataset.json", "w") as f:
    json.dump(dataset, f, indent=4)