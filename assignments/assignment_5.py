import numpy as np
import pandas as pd

# --------------------------------------------------
# LOAD CLEANED EMPLOYEE DATA
# --------------------------------------------------
data = pd.read_csv("output.csv")

# Standardize column names
data.columns = data.columns.str.strip()

# Clean and convert required columns
data["Department"] = (
    data["Department"]
    .astype(str)
    .str.strip()
    .str.upper()
)

data["Join_Date"] = pd.to_datetime(
    data["Join_Date"],
    format="mixed",
    errors="coerce"
)

data["Join_Year"] = data["Join_Date"].dt.year
data["Salary"] = pd.to_numeric(data["Salary"], errors="coerce")
data["Age"] = pd.to_numeric(data["Age"], errors="coerce")

# --------------------------------------------------
# 1. FILTERING
# Employees from IT department earning above 30000
# --------------------------------------------------
it_employees = data[
    (data["Department"] == "IT") &
    (data["Salary"] > 30000)
].copy()

# --------------------------------------------------
# 2. SORTING
# Latest joining year first,
# highest salary first,
# youngest employee first
# --------------------------------------------------
employee_ranking = data.sort_values(
    by=["Join_Year", "Salary", "Age"],
    ascending=[False, False, True]
).copy()

# --------------------------------------------------
# 3. CONDITIONAL SELECTION
# Employees who joined in or before 2018
# --------------------------------------------------
experienced_employees = data.loc[
    data["Join_Year"] <= 2018,
    ["Employee_ID", "Department", "Salary", "Join_Year"]
].copy()

# --------------------------------------------------
# 4. CREATE CONDITIONAL COLUMN
# --------------------------------------------------
data["Bonus_Eligible"] = np.where(
    data["Join_Year"] <= 2018,
    "Yes",
    "No"
)

# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------
print("\n" + "=" * 65)
print(" EMPLOYEE DATA ANALYSIS")
print("=" * 65)

# Result 1
print("\n[1] IT EMPLOYEES WITH SALARY ABOVE 30,000")
print("-" * 65)
if len(it_employees) > 0:
    print(it_employees.to_string(index=False))
else:
    print("No matching employees found.")

# Result 2
print("\n[2] EMPLOYEES SORTED BY JOIN YEAR AND SALARY")
print("-" * 65)
print(employee_ranking.to_string(index=False))

# Result 3
print("\n[3] EMPLOYEES JOINED ON OR BEFORE 2018")
print("-" * 65)
if len(experienced_employees) > 0:
    print(experienced_employees.to_string(index=False))
else:
    print("No matching employees found.")

# Result 4
print("\n[4] BONUS ELIGIBILITY")
print("-" * 65)
print(
    data[
        [
            "Employee_ID",
            "Department",
            "Join_Year",
            "Salary",
            "Bonus_Eligible"
        ]
    ].to_string(index=False)
)

print("\n" + "=" * 65)
print(" ANALYSIS COMPLETED")
print("=" * 65)
