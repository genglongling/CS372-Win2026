import json
import subprocess

def load_json(file_path):
    """Loads seed data from a JSON file."""
    with open(file_path, 'r') as f:
        seeds = json.load(f)
    return seeds

def save_json(file_path, data):
    """Saves seed data to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def call_gemini_cli(prompt: str) -> str:
    """
    Calls the Gemini CLI with a given prompt and returns the response.

    Args:
        prompt: The input prompt for the Gemini CLI.

    Returns:
        The response from the Gemini CLI as a string.
    """
    command = ["gemini", "-p", prompt] # "--model", "gemini-3-flash-preview",
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Gemini CLI command failed with exit code {e.returncode}. Stderr: {e.stderr}")
        return None
    return result.stdout.strip()

def parse_json(response):
    if response is None:
        print("Skipping due to CLI error:\n", response)
        return None
    stripped = response.split('```')
    if len(stripped) == 3:
        stripped = stripped[1]
    elif len(stripped) == 1:
        stripped = stripped[0]
    else:
        print("Skipping due to unexpected formatting in response:\n", response)
        return None
    stripped = stripped.strip('json \n')
    try: 
        parsed_response = json.loads(stripped)
    except json.JSONDecodeError:
        print("Skipping due to JSON decode error:\n", response)
        return None
    return parsed_response