
import numpy as np import pandas as pd

# -------------------------------------------------# EXPERIMENT 2 # DATA CLEANING AND TRANSFORMATION # --------------------------------------------------

# Load employee dataset file_path = r"C:\Users\CC\Downloads\employee_data_100.csv"

employee_df = pd.read_csv(file_path)

print("=" * 65)

print("

EMPLOYEE DATA CLEANING AND TRANSFORMATION")

print("=" * 65)

# -------------------------------------------------# 1. CHECK AND REMOVE DUPLICATE RECORDS # --------------------------------------------------

duplicate_rows = employee_df.duplicated().sum()

print("\n[1] DUPLICATE RECORD CHECK") print("-" * 65) print("Duplicate records detected :", duplicate_rows)

clean_df = employee_df.drop_duplicates().copy()

print("Rows before cleaning print("Rows after cleaning

:", len(employee_df)) :", len(clean_df))

# -------------------------------------------------# 2. CHECK MISSING VALUES # --------------------------------------------------
print("\n[2] MISSING VALUE CHECK") print("-" * 65)
missing_values = clean_df.isnull().sum()
print(missing_values.to_string())
# -------------------------------------------------# 3. FILL MISSING AGE VALUES # --------------------------------------------------
print("\n[3] HANDLING MISSING AGE VALUES") print("-" * 65)
age_median = clean_df["Age"].median()
print("Median Age :", age_median)
clean_df["Age"] = clean_df["Age"].fillna(age_median)
print("Missing Age values after filling :", clean_df["Age"].isnull().sum())
# -------------------------------------------------# 4. CONVERT JOIN DATE # --------------------------------------------------
print("\n[4] DATE CONVERSION") print("-" * 65)
clean_df["Join_Date"] = pd.to_datetime( clean_df["Join_Date"]
)
print("Join_Date converted to datetime format.")
# -------------------------------------------------# 5. SPLIT FULL NAME # --------------------------------------------------
print("\n[5] NAME TRANSFORMATION") print("-" * 65)
clean_df[["First_Name", "Last_Name"]] = ( clean_df["Full Name"] .str.split(" ", n=1, expand=True)
)
print("Full Name separated into First_Name and Last_Name.")
# -------------------------------------------------# 6. EXTRACT JOIN YEAR

# --------------------------------------------------

print("\n[6] EXTRACTING JOIN YEAR") print("-" * 65)

clean_df["Join_Year"] = clean_df["Join_Date"].dt.year

print("Join_Year column created successfully.")

# -------------------------------------------------# 7. REMOVE ORIGINAL FULL NAME COLUMN # --------------------------------------------------

clean_df = clean_df.drop( columns=["Full Name"]
)

# -------------------------------------------------# 8. ARRANGE COLUMNS # --------------------------------------------------

column_order = [ "Employee_ID", "First_Name", "Last_Name", "Department", "Age", "Salary", "Join_Date", "Join_Year"
]

clean_df = clean_df[column_order]

# -------------------------------------------------# 9. FINAL DATA TYPES # --------------------------------------------------

print("\n[7] FINAL DATA TYPES") print("-" * 65)

print(clean_df.dtypes)

# -------------------------------------------------# 10. FINAL DATASET # --------------------------------------------------

print("\n[8] FINAL CLEANED DATASET") print("-" * 65)

print(clean_df.head(10).to_string(index=False))

print("\n" + "=" * 65)

print("

DATA CLEANING COMPLETED SUCCESSFULLY")

print("=" * 65)

import pandas as pd

# -------------------------------------------------# EXPERIMENT 2 # CLEANING DIRTY EMPLOYEE DATA # --------------------------------------------------

source_file = r"C:\Users\CC\Downloads\employee_dirty_data_30 - Copy.csv"

employees = pd.read_csv(source_file)

print("\n" + "=" * 60)

print("

EMPLOYEE DATA CLEANING REPORT")

print("=" * 60)

# -------------------------------------------------# 1. IMPORTED DATA # --------------------------------------------------

print("\n1. ORIGINAL DATASET") print("-" * 60)

print("Total records :", employees.shape[0]) print("Total columns :", employees.shape[1])

print("\nSample records:") print(employees.head().to_string(index=False))

# -------------------------------------------------# 2. FIND AND REMOVE DUPLICATES # --------------------------------------------------

print("\n2. DUPLICATE RECORDS") print("-" * 60)

duplicates = employees.duplicated().sum()

print("Duplicate records found :", duplicates)

employees = employees.drop_duplicates().reset_index(drop=True)

print("Records after removal :", len(employees))

# -------------------------------------------------# 3. CHECK MISSING DATA # --------------------------------------------------

print("\n3. MISSING DATA BEFORE CLEANING") print("-" * 60)

missing = employees.isna().sum()

print(missing.to_string())

# -------------------------------------------------# 4. REPLACE MISSING AGE # --------------------------------------------------

print("\n4. AGE CLEANING") print("-" * 60)

age_value = employees["Age"].median()

employees["Age"] = ( employees["Age"] .fillna(age_value) .astype(int)
)

print("Median age used :", age_value)

print("Missing Age

:", employees["Age"].isna().sum())

# -------------------------------------------------# 5. REPLACE MISSING SALARY # --------------------------------------------------

print("\n5. SALARY CLEANING") print("-" * 60)

salary_value = employees["Salary"].mean()

employees["Salary"] = employees["Salary"].fillna( salary_value
)

print("Mean salary used :", round(salary_value, 2)) print("Missing Salary :", employees["Salary"].isna().sum())

# -------------------------------------------------# 6. CLEAN DEPARTMENT # --------------------------------------------------

print("\n6. DEPARTMENT CLEANING") print("-" * 60)

employees["Department"] = ( employees["Department"] .fillna("Unassigned") .str.strip() .str.title()
)

print("Department names cleaned successfully.")

# -------------------------------------------------# 7. CLEAN EMPLOYEE NAMES # --------------------------------------------------

print("\n7. NAME CLEANING") print("-" * 60)
employees["Full Name"] = ( employees["Full Name"] .fillna("Unknown") .str.strip() .str.title()
)
# Separate first and last names name_parts = employees["Full Name"].str.split(
" ", n=1, expand=True )
employees["First_Name"] = name_parts[0]
employees["Last_Name"] = ( name_parts[1] if name_parts.shape[1] > 1 else ""
)
# -------------------------------------------------# 8. PROCESS JOIN DATE # --------------------------------------------------
print("\n8. DATE PROCESSING") print("-" * 60)
employees["Join_Date"] = pd.to_datetime( employees["Join_Date"], format="mixed", errors="coerce"
)
employees["Join_Year"] = ( employees["Join_Date"] .dt.year .astype("Int64")
)
print("Join dates converted successfully.") print("Join year column created.")
# -------------------------------------------------# 9. REMOVE UNNECESSARY COLUMN # --------------------------------------------------
employees.drop( columns=["Full Name"], inplace=True
)

# -------------------------------------------------# 10. ARRANGE FINAL COLUMNS # --------------------------------------------------

final_columns = [ "Employee_ID", "First_Name", "Last_Name", "Department", "Age", "Salary", "Join_Date", "Join_Year"
]

employees = employees[ [col for col in final_columns if col in employees.columns]
]

# -------------------------------------------------# 11. FINAL RESULT # --------------------------------------------------

print("\n" + "=" * 60)

print("

CLEANED EMPLOYEE DATA")

print("=" * 60)

print(employees.to_string(index=False))

# -------------------------------------------------# 12. DATA TYPES # --------------------------------------------------

print("\n" + "=" * 60)

print("

FINAL DATA TYPES")

print("=" * 60)

print(employees.dtypes.to_string())

# -------------------------------------------------# 13. SAVE CLEANED DATA # --------------------------------------------------

output_file = "cleaned_employee_data.csv"

employees.to_csv( output_file, index=False
)

print("\n" + "=" * 60) print("Cleaning completed successfully!") print("Output file :", output_file) print("=" * 60)

import numpy as np import pandas as pd

# -------------------------------------------------# LOAD CLEANED EMPLOYEE DATA # --------------------------------------------------

data = pd.read_csv("output.csv")

# Standardize column names data.columns = data.columns.str.strip()

# Clean and convert required data["Department"] = (
data["Department"] .astype(str) .str.strip() .str.upper() )

columns

data["Join_Date"] = pd.to_datetime( data["Join_Date"], format="mixed", errors="coerce"
)

data["Join_Year"] = data["Join_Date"].dt.year

data["Salary"] = pd.to_numeric( data["Salary"], errors="coerce"
)

data["Age"] = pd.to_numeric( data["Age"], errors="coerce"
)

# -------------------------------------------------# 1. FILTERING # Employees from IT department earning above 30000 # --------------------------------------------------

it_employees = data[ (data["Department"] == "IT") & (data["Salary"] > 30000)
].copy()

# -------------------------------------------------# 2. SORTING # Latest joining year first, # highest salary first, # youngest employee first # --------------------------------------------------

employee_ranking = data.sort_values( by=["Join_Year", "Salary", "Age"], ascending=[False, False, True]
).copy()

# -------------------------------------------------# 3. CONDITIONAL SELECTION # Employees who joined in or before 2018 # --------------------------------------------------

experienced_employees = data.loc[ data["Join_Year"] <= 2018, ["Employee_ID", "Department", "Salary", "Join_Year"]
].copy()

# -------------------------------------------------# 4. CREATE CONDITIONAL COLUMN # --------------------------------------------------

data["Bonus_Eligible"] = data["Join_Year"] <= "Yes", "No"
)

np.where( 2018,

# -------------------------------------------------# DISPLAY RESULTS # --------------------------------------------------

print("\n" + "=" * 65)

print("

EMPLOYEE DATA ANALYSIS")

print("=" * 65)

# Result 1 print("\n[1] IT EMPLOYEES WITH SALARY ABOVE 30,000") print("-" * 65)

if len(it_employees) > 0: print(it_employees.to_string(index=False))
else: print("No matching employees found.")

# Result 2 print("\n[2] EMPLOYEES SORTED BY JOIN YEAR AND SALARY") print("-" * 65)

print(employee_ranking.to_string(index=False))

# Result 3 print("\n[3] EMPLOYEES JOINED ON OR BEFORE 2018") print("-" * 65)

if len(experienced_employees) > 0: print(experienced_employees.to_string(index=False))
else: print("No matching employees found.")

# Result 4 print("\n[4] BONUS ELIGIBILITY") print("-" * 65)

print( data[ [ "Employee_ID", "Department", "Join_Year", "Salary", "Bonus_Eligible" ] ].to_string(index=False)
)

print("\n" + "=" * 65)

print("

ANALYSIS COMPLETED")

print("=" * 65)

import pandas as pd

