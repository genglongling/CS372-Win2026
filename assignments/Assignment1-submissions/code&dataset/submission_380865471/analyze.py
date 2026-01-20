from util import *
from collections import defaultdict
import pandas as pd

def to_latex(data):
    keys = []
    values = []
    for key, value in data.items():
        keys.append(key)
        values.append(value)
    return pd.DataFrame([keys, values]).T.to_latex(index=False, header=False)


if __name__ == "__main__":
    cases = load_json("finished.json")

    labels = defaultdict(lambda: 0)
    traps = defaultdict(lambda: 0)
    subdomains = defaultdict(lambda: 0)
    difficulties = defaultdict(lambda: 0)
    pearl_levels = defaultdict(lambda: 0)
    has_subtype = defaultdict(lambda: 0)
    
    for gen in cases:
        pearl_levels[gen['annotations']['pearl_level']] += 1
        labels[gen['label']] += 1
        traps[gen['annotations']['trap_type']] += 1
        subdomains[gen['annotations']['subdomain']] += 1
        difficulties[gen['annotations']['difficulty']] += 1
        has_subtype['trap_subtype' in gen['annotations']] += 1
        gen['annotations']['bucket'] = "BucketLarge-C"
        gen['annotations']['domain'] = "D7 (Law)"
        gen['annotations']['author'] = "mhayes3@stanford.edu"
    
    print("Total new cases\n", len(cases))
    print("Pearl levels\n", to_latex(pearl_levels))
    print("Label distribution\n", to_latex(labels))
    print("Trap distribution\n", to_latex(traps))
    print("Subdomain distribution\n", to_latex(subdomains))
    print("Difficulty distribution\n", to_latex(difficulties))
    print("Has subtype\n", to_latex(has_subtype))
    save_json("finished.json", cases)