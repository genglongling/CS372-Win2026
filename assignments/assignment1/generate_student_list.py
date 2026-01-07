#!/usr/bin/env python3
"""
Script to convert Studentlist.csv to LaTeX table format for assignment1.tex
CSV format: First Name, Last Name, Email
"""

import sys
import os
import csv

# Path to the CSV file (in root directory)
csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Studentlist.csv')

if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found")
    print("Please ensure Studentlist.csv exists in the root directory with columns: First Name, Last Name, Email")
    sys.exit(1)

try:
    # Read CSV file
    latex_rows = []
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Check if required columns exist
        if 'First Name' not in reader.fieldnames or 'Last Name' not in reader.fieldnames or 'Email' not in reader.fieldnames:
            print("Error: CSV file must contain columns: 'First Name', 'Last Name', 'Email'")
            print(f"Found columns: {reader.fieldnames}")
            sys.exit(1)
        
        for row in reader:
            first_name = row['First Name'].strip() if row['First Name'] else ""
            last_name = row['Last Name'].strip() if row['Last Name'] else ""
            email = row['Email'].strip() if row['Email'] else ""
            
            # Skip empty rows
            if not first_name or not last_name:
                continue
            
            # Escape LaTeX special characters
            first_name = first_name.replace('&', '\\&').replace('_', '\\_').replace('%', '\\%').replace('$', '\\$')
            last_name = last_name.replace('&', '\\&').replace('_', '\\_').replace('%', '\\%').replace('$', '\\$')
            email = email.replace('&', '\\&').replace('_', '\\_').replace('%', '\\%').replace('$', '\\$')
            
            latex_rows.append(f"{first_name} & {last_name} & {email} \\\\")
    
    # Print LaTeX code
    print("% Student list generated from Studentlist.csv")
    print("% Copy the following lines into the assignment1.tex file in the longtable section")
    print()
    for row in latex_rows:
        print(row)
    
    print(f"\n% Total students: {len(latex_rows)}")
    
except Exception as e:
    print(f"Error processing CSV file: {e}")
    sys.exit(1)

