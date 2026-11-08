import duckdb

con = duckdb.connect("papers.duckdb")

con.execute("""
CREATE OR REPLACE TABLE papers AS
SELECT *
FROM read_parquet('papers_clean.parquet')
""")

print("Table created successfully!")

# 1. Total papers
print("\nTotal papers:")
print(
    con.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
)

# 2. Papers by category
print("\nPapers by category:")
print(
    con.execute("""
        SELECT category, COUNT(*) AS paper_count
        FROM papers
        GROUP BY category
        ORDER BY paper_count DESC
    """).fetchall()
)

# 3. Latest papers
print("\nLatest 10 papers:")
print(
    con.execute("""
        SELECT paper_id, title, published, category
        FROM papers
        ORDER BY published DESC
        LIMIT 10
    """).fetchall()
)

# 4. Papers by publication year
print("\nPapers by publication year:")
print(
    con.execute("""
        SELECT
            EXTRACT(YEAR FROM CAST(published AS TIMESTAMP)) AS year,
            COUNT(*) AS paper_count
        FROM papers
        GROUP BY year
        ORDER BY year DESC
    """).fetchall()
)

con.close()