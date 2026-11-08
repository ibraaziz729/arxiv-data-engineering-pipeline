import pandas as pd

df = pd.read_parquet("papers_clean.parquet")

df["published"] = pd.to_datetime(df["published"], errors="coerce")
df["publication_year"] = df["published"].dt.year
df["publication_month"] = df["published"].dt.month

df["category"] = df["category"].astype(str).str.strip()
df["title"] = df["title"].astype(str).str.strip()
df["title_length"] = df["title"].str.len()

df = df[
    [
        "paper_id",
        "title",
        "published",
        "publication_year",
        "publication_month",
        "category",
        "title_length",
    ]
]

df.to_parquet("papers_transformed.parquet", index=False)

print("Transformation completed successfully!")
print("Rows:", len(df))
print("Columns:", df.columns.tolist())
print("Saved: papers_transformed.parquet")