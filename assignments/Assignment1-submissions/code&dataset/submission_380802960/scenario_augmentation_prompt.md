# Context

We have a dataset of existing scenarios. Each of the scenarios has some kind of a causal mechanism behind it. Imagine you are someone aware of Pearl's Causality Hierarchy. For context, let us elucidate what the PCH is about. 

## Pearl's Causality Hierarchy 
Pearl's Causality Hierarchy has three levels of increasingly sophisticated reasoning:

- Level 1 - Association (Seeing): Basic statistical relationships from data. Answers "What is?" questions like correlations and predictions. Example: "Students who study more tend to get better grades."

- Level 2 - Intervention (Doing): Understanding what happens when we actively change something. Answers "What if?" questions about cause and effect. Example: "What if we force students to study 2 extra hours - will grades improve?"

- Level 3 - Counterfactuals (Imagining): Reasoning about alternative scenarios that didn't happen. Answers "What if things had been different?" Example: "Would this specific student have passed if they had studied more?"

Now, we wish to perform data augmentation on top of the scenarios. Your task is to go through each scenario in a provided markdown file. Each scenario acts as a parent seed. For each seed, I want you to think of 5 new child examples from daily life where the same causal mechanism exists as in the scenario, but the domain where it is being applied is very different. The child and parent example should share distinctions, and the child should not just be changing the parent in a trivial way (for example, changing from "dog" in parent to "cat" in child will not suffice). Further, the child examples should also not borrow too much from other scenarios in the same file, although a minimal level of overlap is fine. 

# Process

- Each scenario in the markdown file will start with a "#" heading and will have an associated number (for example, Scenario 11)
- You need to create a new markdown file which copies the initial scenario under "#" heading. 
- Below it, explain the underlying causal mechanism in strictly three lines (50 words) or lesser and save it under "## Scenario X - Causal Mechanism" heading. 
- Then save all the child scenarios under another "## Scenario X - Child Scenarios" heading. 
- Under this heading each child scenario should be saved under "###" heading and named as "### Scenario 11.1", "#Scenario 11.2" and so on
