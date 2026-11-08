import pandas as pd

df = pd.read_csv("papers_clean.csv")

df.to_parquet("papers_clean.parquet", index=False)

print("Rows:", len(df))
print("Saved: papers_clean.parquet")