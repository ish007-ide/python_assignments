exp

file_path = r"C:\Users\CC\Downloads\emp_data.csv" df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

print("Original DataFrame:") print(df)

print("\n" + "=" * 80)

# Concept 1 print("\nConcept 1: Average Salary & Bonus per Department\n")

dept_means = ( df.groupby("Department")[["Salary", "Bonus_Eligible"]]

.mean() .round(2) )
print(dept_means)
print("\n" + "=" * 80)
# Concept 2 print("\nConcept 2: Average Salary & Performance by Department & Role\n")
role_hierarchy = ( df.groupby(["Department", "Role"])[["Salary", "Performance_Rating"]] .mean() .round(2)
)
print(role_hierarchy)
print("\n" + "=" * 80)
# Concept 3 print("\nConcept 3: Advanced Aggregation\n")
dept_summary = ( df.groupby("Department") .agg( Salary_Mean=("Salary", "mean"), Salary_Min=("Salary", "min"), Salary_Max=("Salary", "max"), Total_Bonus=("Bonus_Eligible", "sum"),

Avg_Performance=("Performance_Rating", "mean") ) .round(2) )
print(dept_summary)
print("\n" + "=" * 80)
# Concept 4 print("\nConcept 4: Department Report\n")
clean_dept_report = ( df.groupby("Department") .agg( Total_Employees=("Employee_ID", "count"), Total_Payroll=("Salary", "sum"), Average_Salary=("Salary", "mean"), Highest_Bonus=("Bonus_Eligible", "max"), Average_Performance=("Performance_Rating", "mean") ) .reset_index() .round(2)
)
print(clean_dept_report.to_string(index=False))
print("\n" + "=" * 80)
# Concept 5 print("\nConcept 5: Departments with Payroll > 200000\n")

high_payroll_dept = df.groupby("Department").filter( lambda x: x["Salary"].sum() > 200000
)
result = high_payroll_dept[ ["Department", "Full Name", "Role", "Salary"]
]
print(result.to_string(index=False))\ dex=False))
exp7

import matplotlib.pyplot as plt

# -------------------------------------------------# SAMPLE STUDENT DATA # --------------------------------------------------

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] study_time = [2, 3, 2.5, 4, 6]

student_names = ["Aarav", "Diya", "Rohan", "Meera"] assignments = [5, 8, 4, 7]

marks = [48, 55, 61, 64, 68, 72, 76, 81, 87, 92]

# -------------------------------------------------# CREATE THREE SUBPLOTS # --------------------------------------------------

figure, chart = plt.subplots( 1, 3, figsize=(15, 5)
)

figure.suptitle( "Student Academic fontsize=16, fontweight="bold"
)

Performance",

# -------------------------------------------------# 1. LINE GRAPH # --------------------------------------------------
chart[0].plot( weekdays, study_time, marker="o", markersize=8, color="#2563EB", linewidth=2.5
)
chart[0].set_title( "Daily Study Time", fontsize=12, fontweight="bold"
)
chart[0].set_xlabel("Day") chart[0].set_ylabel("Study Hours")
chart[0].grid( True, linestyle="--", alpha=0.5
)
# -------------------------------------------------# 2. BAR GRAPH # --------------------------------------------------
chart[1].bar( student_names, assignments, color=[ "#FF6B6B", "#4ECDC4", "#FFD166", "#6C5CE7" ], edgecolor="black", linewidth=0.7
)
chart[1].set_title( "Assignments Completed", fontsize=12, fontweight="bold"
)
chart[1].set_xlabel("Students") chart[1].set_ylabel("Number of Assignments")
# Display values on bars for i, value in enumerate(assignments):

chart[1].text( i, value + 0.2, str(value), ha="center", fontweight="bold"
)
# -------------------------------------------------# 3. HISTOGRAM # --------------------------------------------------
chart[2].hist( marks, bins=[40, 50, 60, 70, 80, 90, 100], color="#8E44AD", edgecolor="white", linewidth=1.5
)
chart[2].set_title( "Exam Score Distribution", fontsize=12, fontweight="bold"
)
chart[2].set_xlabel("Marks") chart[2].set_ylabel("Number of Students")
chart[2].grid( axis="y", linestyle="--", alpha=0.4
)
# -------------------------------------------------# FINAL FORMATTING # --------------------------------------------------
plt.tight_layout()
plt.show()
