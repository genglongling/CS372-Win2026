# Student List Instructions

## Overview

The student list is stored in `Studentlist.csv` in the root directory with the following columns:
- **First Name**
- **Last Name**  
- **Email** (format: Login ID + @stanford.edu)

## CSV Format

The CSV file should have a header row and be formatted as:
```csv
First Name,Last Name,Email
John,Doe,jdoe@stanford.edu
Jane,Smith,jsmith@stanford.edu
```

## Generating LaTeX Table from CSV

To convert the CSV file to LaTeX table format for `assignment1.tex`:

1. **Run the script:**
   ```bash
   cd assignments/assignment1
   python3 generate_student_list.py
   ```

2. **Copy the output:**
   - The script will output LaTeX table rows
   - Copy all the generated rows
   - Paste them into `assignment1.tex` in the `\endlastfoot` section (replace the comment `% Student entries will be added here`)

## Manual Entry

Alternatively, you can manually add students to the table in `assignment1.tex` using the format:
```latex
First Name & Last Name & loginid@stanford.edu \\
```

## Notes

- The Email column should already be in the format `loginid@stanford.edu` in the CSV file
- Special LaTeX characters (like `&`, `_`, `%`, `$`) will be automatically escaped by the script
- The table uses `longtable` package to handle multiple pages if needed
- The CSV file should use UTF-8 encoding

