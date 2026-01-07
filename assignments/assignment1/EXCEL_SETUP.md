# Excel File Setup Instructions

## Adding Columns to Studentlist.xlsx

To add the required columns (First Name, Last Name, Email) to your `Studentlist.xlsx` file:

### Option 1: Using the Python Script (Recommended)

1. **Install openpyxl** (if not already installed):
   ```bash
   pip3 install openpyxl
   ```

2. **Run the setup script:**
   ```bash
   cd assignments/assignment1
   python3 setup_studentlist_columns.py
   ```

   This script will:
   - Check if the columns exist
   - Add "First Name", "Last Name", and "Email" columns if they're missing
   - Preserve any existing data

### Option 2: Manual Setup in Excel

1. Open `Studentlist.xlsx` in Excel or Google Sheets
2. Ensure the first row contains headers
3. Add or verify these three columns in order:
   - **Column A:** First Name
   - **Column B:** Last Name
   - **Column C:** Email
4. Save the file

### Column Format

- **First Name:** Student's first name
- **Last Name:** Student's last name
- **Email:** Should be in format `loginid@stanford.edu` (Login ID + @stanford.edu)

### Example Structure

| First Name | Last Name | Email |
|------------|-----------|-------|
| John       | Doe       | jdoe@stanford.edu |
| Jane       | Smith     | jsmith@stanford.edu |

### Next Steps

After setting up the columns:
1. Add student data to the Excel file
2. Later, you can convert to CSV format if needed
3. Use `generate_student_list.py` to generate LaTeX table code

