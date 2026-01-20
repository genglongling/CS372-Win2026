#!/usr/bin/env python3
"""
Extract JSON examples from markdown file and save to a single JSON dataset.
"""

import json
import re
import sys

def extract_json_from_markdown(markdown_file, output_file):
    """
    Extract all JSON objects from markdown code blocks and save to a JSON array.
    
    Args:
        markdown_file: Path to the input markdown file
        output_file: Path to the output JSON file
    """
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match code blocks that contain JSON
    # Matches ```python followed by { ... } followed by ```
    pattern = r'```python\s*(\{.*?\})\s*```'
    
    # Use re.DOTALL to make . match newlines
    matches = re.findall(pattern, content, re.DOTALL)
    
    json_objects = []
    errors = []
    
    for i, json_str in enumerate(matches, 1):
        try:
            # Clean up common JSON issues: trailing commas before closing braces/brackets
            # Remove trailing commas before } or ]
            json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
            
            # Parse the JSON string
            json_obj = json.loads(json_str)
            json_objects.append(json_obj)
        except json.JSONDecodeError as e:
            error_msg = f"Error parsing JSON #{i}: {str(e)}"
            errors.append(error_msg)
            print(f"Warning: {error_msg}", file=sys.stderr)
            # Try to show a snippet of the problematic JSON
            snippet = json_str[:200] if len(json_str) > 200 else json_str
            print(f"  JSON snippet: {snippet}...", file=sys.stderr)
    
    # Save all JSON objects to a single file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_objects, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully extracted {len(json_objects)} JSON objects")
    if errors:
        print(f"Encountered {len(errors)} parsing errors", file=sys.stderr)
    
    return len(json_objects)

if __name__ == "__main__":
    input_file = "claude_generated_jsons.md"
    output_file = "dataset.json"
    
    count = extract_json_from_markdown(input_file, output_file)
    print(f"Saved {count} JSON objects to {output_file}")

