import re

with open('bucket_E.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all scenarios: from "Scenario." to "Variables." or "Variable."
pattern = r'Scenario\.\s*(.*?)\s*Variables?\.'
scenarios = re.findall(pattern, content, re.DOTALL)

# Write to output file
with open('scenarios_output.md', 'w', encoding='utf-8') as f:
    for i, scenario in enumerate(scenarios, 1):
        f.write(f"# Scenario {i}\n\n{scenario.strip()}\n\n")

print(f"Extracted {len(scenarios)} scenarios to scenarios_output.md")

