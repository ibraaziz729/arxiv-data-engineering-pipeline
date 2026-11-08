import pandas as pd

df = pd.read_csv("papers.csv")

print("Original rows:", len(df))
print("Columns:", df.columns.tolist())

df = df.drop_duplicates(subset="paper_id")

df = df.dropna(subset=["paper_id", "title"])

df["title"] = df["title"].str.strip()

df.to_csv("papers_clean.csv", index=False)

print("Clean rows:", len(df))
print("Saved: papers_clean.csv")