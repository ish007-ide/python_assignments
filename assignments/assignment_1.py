
# Load CSV file file_path = r"C:\Users\CC\Downloads\annul_data.csv" data = pd.read_csv(file_path)

print("\n" + "#" * 65)

print("

CSV DATA EXPLORATION REPORT")

print("#" * 65)

# -------------------------------------------------# 1. DATASET PREVIEW # --------------------------------------------------

print("\n[1] DATASET PREVIEW") print("-" * 65)

print(data.head(5).to_string(index=False))

# -------------------------------------------------# 2. SIZE OF DATASET # --------------------------------------------------

print("\n[2] DATASET SIZE") print("-" * 65)

rows, columns = data.shape

print("Total records :", rows) print("Total fields :", columns)

# -------------------------------------------------# 3. FIELD INFORMATION # --------------------------------------------------

print("\n[3] FIELD INFORMATION") print("-" * 65)

for number, column in enumerate(data.columns, start=1): print( f"{number:>2}. " f"{column:<25} " f"{str(data[column].dtype)}" )

# -------------------------------------------------# 4. DATASET STRUCTURE # --------------------------------------------------

print("\n[4] DATASET STRUCTURE")

print("-" * 65)
print("Index range :", data.index.min(), "to", data.index.max()) print("Memory used :", round(
data.memory_usage(deep=True).sum() / 1024, 2 ), "KB")
# -------------------------------------------------# 5. NULL VALUE ANALYSIS # --------------------------------------------------
print("\n[5] NULL VALUE ANALYSIS") print("-" * 65)
null_values = data.isna().sum()
if null_values.sum() == 0: print("No NULL values are present in the dataset.")
else: for column, count in null_values.items(): if count > 0: print(f"{column:<25} : {count}")
# -------------------------------------------------# 6. DUPLICATE ANALYSIS # --------------------------------------------------
print("\n[6] DUPLICATE RECORD ANALYSIS") print("-" * 65)
duplicate_count = data.duplicated().sum()
print("Duplicate records :", duplicate_count)
# -------------------------------------------------# 7. NUMERICAL ANALYSIS # --------------------------------------------------
print("\n[7] NUMERICAL DATA ANALYSIS") print("-" * 65)
numeric_columns = data.select_dtypes( include="number"
).columns
if len(numeric_columns) > 0: numerical_summary = data[numeric_columns].describe().T
print( numerical_summary[ ["count", "mean", "std", "min", "max"] ].round(2).to_string()
)

else: print("No numerical fields available.")
# -------------------------------------------------# 8. CATEGORICAL ANALYSIS # --------------------------------------------------
print("\n[8] CATEGORICAL DATA ANALYSIS") print("-" * 65)
categorical_columns = data.select_dtypes( include=["object", "category", "string"]
).columns
if len(categorical_columns) > 0:
for column in categorical_columns: print(f"\nColumn : {column}") print("Unique values :", data[column].nunique()) print("Most common :", data[column].mode()[0])
else: print("No categorical fields available.")
# -------------------------------------------------# 9. FREQUENCY ANALYSIS # --------------------------------------------------
print("\n[9] CATEGORY FREQUENCY ANALYSIS") print("-" * 65)
if len(categorical_columns) > 0:
for column in categorical_columns:
print(f"\n>>> {column}") print(data[column].value_counts().head(10).to_string())
else: print("No categorical fields available.")
# -------------------------------------------------# 10. STATISTICAL METRICS # --------------------------------------------------
print("\n[10] STATISTICAL METRICS") print("-" * 65)
if len(numeric_columns) > 0:
statistics = pd.DataFrame({ "Average": data[numeric_columns].mean(), "Middle Value": data[numeric_columns].median(),

"Variance": data[numeric_columns].var(), "Asymmetry": data[numeric_columns].skew() })

print(statistics.round(2).to_string())

else: print("No numerical fields available.")

# -------------------------------------------------# COMPLETION # --------------------------------------------------

print("\n" + "#" * 65)

print("

DATA ANALYSIS FINISHED")

print("#" * 65)

