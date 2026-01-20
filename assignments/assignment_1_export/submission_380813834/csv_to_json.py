#!/usr/bin/env python3
"""
CSV to JSON Converter

This script reads a CSV file and converts it to JSON format.
The first row of the CSV file is used as field names (keys),
and subsequent rows are converted to JSON objects.
"""

import csv
import json
import sys
import argparse


def csv_to_json(csv_file_path, json_file_path=None, indent=2):
    """
    Convert CSV file to JSON format.
    
    Args:
        csv_file_path: Path to the input CSV file
        json_file_path: Path to the output JSON file (optional)
        indent: Number of spaces for JSON indentation (default: 2)
    
    Returns:
        List of dictionaries representing the CSV data
    """
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            # Read CSV and convert to list of dictionaries
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        # Convert to JSON
        json_data = json.dumps(data, indent=indent)
        
        # Write to file or print to stdout
        if json_file_path:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
            print(f"Successfully converted {csv_file_path} to {json_file_path}")
        else:
            print(json_data)
        
        return data
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Convert CSV file to JSON format. First row contains field names.'
    )
    parser.add_argument(
        'csv_file',
        help='Path to the input CSV file'
    )
    parser.add_argument(
        '-o', '--output',
        dest='json_file',
        help='Path to the output JSON file (if not specified, prints to stdout)'
    )
    parser.add_argument(
        '-i', '--indent',
        type=int,
        default=2,
        help='Number of spaces for JSON indentation (default: 2)'
    )
    
    args = parser.parse_args()
    csv_to_json(args.csv_file, args.json_file, args.indent)


if __name__ == '__main__':
    main()
