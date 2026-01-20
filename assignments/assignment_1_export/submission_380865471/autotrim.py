from util import * 
import copy

def get_case(generated, id):
    for item in generated:
        if item['seed']['annotations']['case_id'] == id:
            return item
        for gen in item['generated']:
            if gen['annotations']['case_id'] == id:
                return gen
    raise ValueError(f"Case ID {id} not found")

def yes_keep(gen):
    return 'review' in gen and 'keep' in gen['review'] and 'YES' in gen['review']['keep']


def no_keep(gen):
    return 'review' in gen and 'keep' in gen['review'] and 'NO' in gen['review']['keep']

def no_keep_id(generated, id):
    return no_keep(get_case(generated, id))


def trim_nos(generated):
    result = copy.deepcopy(generated)
    for seed in result:
        new_generated = []
        for gen in seed['generated']:
            if not no_keep(gen):
                new_similar = []
                for similar in gen['similar_cases']:
                    if not no_keep_id(generated, similar['case_id']):
                        new_similar.append(similar)
                gen['similar_cases'] = new_similar
                new_generated.append(gen)
        seed['generated'] = new_generated
    return result
                

def get_high_dupe_count(gen):
    if 'similar_cases' not in gen:
        return 0
    if yes_keep(gen):
        return 0
    if no_keep(gen):
        return 999999999
    count = 0
    for similar in gen['similar_cases']:
        if similar['similarity'] == 'HIGH' and not 'is_resolved' in similar:
            count += 1
    return count

def resolve(generated, id):
    gen = get_case(generated, id)
    if not 'review' in gen:
        gen['review'] = {
            'keep': 'NO',
            'reason': "Automatically flagged for high duplicity"
        }
    for seed in generated:
        for gen in seed['generated']:
            if 'similar_cases' in gen:
                for similar in gen['similar_cases']:
                    if similar['case_id'] == id:
                        similar['is_resolved'] = 'TRUE'
    

def get_dupe_counts(generated):
    high_dupe_counts = []
    for original in generated:
        for gen in original['generated']:
            count = get_high_dupe_count(gen)
            high_dupe_counts.append((count, gen['annotations']['case_id']))
    high_dupe_counts.sort(reverse=True)
    return high_dupe_counts

def other_valid_generated_cases(generated, case_id):
    count = 0
    for original in generated:
        for gen in original['generated']:
            if gen['annotations']['case_id'] == case_id:
                continue
            if not no_keep(gen):
                count += 1
    return count


if __name__ == "__main__":
    generated = load_json("generated.json")
    total_trimmed = 0
    trimmed = True
    while trimmed:
        trimmed = False
        not_trimmed = trim_nos(generated)
        dupe_counts = get_dupe_counts(not_trimmed)
        for count, case_id in dupe_counts:
            if count > 1 and other_valid_generated_cases(not_trimmed, case_id) > 1:
                print("Trimming case_id ", case_id)
                resolve(generated, case_id)
                trimmed = True
                total_trimmed += 1
                break
    print("Total trimmed:", total_trimmed)
    save_json("autotrimmed_generated_marked.json", generated)
    save_json("autotrimmed_generated_trimmed.json", trim_nos(generated))


    # finished = load_json("finished.json")
    finished = []
    remaining = []
    reviwed = load_json("autotrimmed_generated_trimmed_reviewed copy.json")
    ambiguous = 0
    positive = 0
    negative = 0
    for seed in reviwed:
        yes = []
        for gen in seed['generated']:
            if yes_keep(gen):
                yes.append(gen)
                if "YES" in gen['label']:
                    positive += 1
                elif "NO" in gen['label']:
                    negative += 1
                elif "AMBIGUOUS" in gen['label']:
                    ambiguous += 1
                else:
                    print("Unknown label:", gen['label'])
        if len(yes) >= 1:
            for gen in yes:
                gen['seed'] = seed['seed']['annotations']['case_id']
            if len(yes) == 1:
                print("Only one YES for seed ", seed['seed']['annotations']['case_id'])
            if len(yes) > 2:
                print(len(yes), " YES for seed ", seed['seed']['annotations']['case_id'])
        else:
            remaining.append(seed)
        finished += yes
    print("None added for")
    for seed in remaining:
        print(seed['seed']['annotations']['case_id'])
    print("total finished:", len(finished))
    print("ambiguous:", ambiguous)
    print("yes:", positive)
    print("no:", negative)
    save_json("finished.json", finished)
    save_json("autotrimmed_generated_trimmed_reviewed.json", remaining)
            
