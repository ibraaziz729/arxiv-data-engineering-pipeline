import pandas as pd

df = pd.read_parquet("papers_clean.parquet")

print("=== DATA QUALITY CHECK ===")

# 1. Row count
print("Total rows:", len(df))

# 2. Required columns
required_columns = ["paper_id", "title", "published", "category"]

for column in required_columns:
    print(f"{column} exists:", column in df.columns)

# 3. Missing values
print("\nMissing values:")
print(df[required_columns].isnull().sum())

# 4. Duplicate IDs
print("\nDuplicate paper IDs:", df["paper_id"].duplicated().sum())

# 5. Empty titles
print("Empty titles:", (df["title"].str.strip() == "").sum())

# Final result
quality_passed = (
    len(df) > 0
    and all(column in df.columns for column in required_columns)
    and df[required_columns].isnull().sum().sum() == 0
    and df["paper_id"].duplicated().sum() == 0
    and (df["title"].str.strip() == "").sum() == 0
)

print("\nDATA QUALITY:", "PASSED" if quality_passed else "FAILED")