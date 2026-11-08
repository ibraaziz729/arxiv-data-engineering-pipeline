import duckdb

con = duckdb.connect("papers.duckdb")

con.execute("""
CREATE OR REPLACE TABLE papers_transformed AS
SELECT *
FROM read_parquet('papers_transformed.parquet')
""")

print("Transformed table created successfully!")

print("\nTotal transformed papers:")
print(
    con.execute(
        "SELECT COUNT(*) FROM papers_transformed"
    ).fetchone()[0]
)

print("\nSample data:")
print(
    con.execute("""
        SELECT
            paper_id,
            title,
            publication_year,
            publication_month,
            category,
            title_length
        FROM papers_transformed
        LIMIT 5
    """).fetchall()
)

con.close()