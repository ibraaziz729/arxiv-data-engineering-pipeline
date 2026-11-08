# Entropy | arXiv Data Engineering project

> An end-to-end data engineering project developed during the Entropy Job Shadowing program, using the arXiv API as the primary data source.

---

## 📌 Project Overview

This project implements an end-to-end data engineering pipeline for collecting, cleaning, validating, transforming, storing, and analyzing research paper metadata from the arXiv API.

The project demonstrates how raw external data can be transformed into a clean, validated, and analytics-ready dataset through a structured and reproducible workflow.

### Data Flow

```text
arXiv API
    ↓
Data Extraction
    ↓
Data Cleaning
    ↓
Data Quality Validation
    ↓
Parquet Storage
    ↓
Data Transformation
    ↓
DuckDB
    ↓
SQL Analytics
```

---

## 🏗️ Architecture

The pipeline is organized into clear data engineering stages:

### 1. Source

**arXiv API**

The arXiv API is used as the primary source for research paper metadata.

The extracted data includes:

- Paper ID
- Title
- Publication date
- Category
- Paper URL

---

### 2. Extraction

**File:** `fetch_papers.py`

Retrieves research paper metadata from the arXiv API and stores the raw dataset locally.

---

### 3. Data Cleaning

**File:** `clean_data.py`

The raw dataset is cleaned before entering the analytical workflow.

The cleaning stage handles:

- Missing values
- Invalid records
- Duplicate paper IDs
- Required fields
- Empty titles

The result is stored as a clean dataset.

---

### 4. Data Quality Validation

**File:** `data_quality.py`

Automated validation checks are performed before continuing through the pipeline.

The validation stage checks:

- Required columns
- Missing values
- Duplicate paper IDs
- Empty titles
- Dataset availability

The implemented validation successfully returned:

```text
DATA QUALITY: PASSED
```

---

### 5. Data Transformation

**File:** `transform_data.py`

The cleaned dataset is transformed into an analytics-ready structure.

Additional analytical fields include:

- `publication_year`
- `publication_month`
- `category`
- `title_length`

These derived fields make the dataset more suitable for analytical queries.

---

### 6. Columnar Storage

**Format:** Apache Parquet

The cleaned and transformed datasets are stored in Parquet format.

Parquet provides an efficient columnar format for storing and processing analytical datasets.

Generated datasets include:

```text
papers_clean.parquet
papers_transformed.parquet
```

---

### 7. Analytical Database

**Files:**

- `load_transformed.py`
- `duckdb_analysis.py`

The transformed Parquet dataset is loaded into **DuckDB**, creating an analytical layer for querying the processed data.

---

### 8. SQL Analytics

SQL is used through DuckDB to perform analytical queries on the final dataset.

The project includes queries for:

- Total number of papers
- Papers by category
- Latest papers
- Papers by publication year
- Sample analytical records

Example:

```sql
SELECT
    publication_year,
    COUNT(*) AS paper_count
FROM papers
GROUP BY publication_year
ORDER BY publication_year DESC;
```

---

## ⚙️ Pipeline Automation

**File:** `pipeline.py`

The project includes a Python-based pipeline runner that executes the main processing stages sequentially.

```text
Extraction
    ↓
Cleaning
    ↓
Validation
    ↓
Transformation
    ↓
Loading
    ↓
Analytics
```

A successful execution produces:

```text
PIPELINE COMPLETED SUCCESSFULLY
```

This provides a reproducible workflow for running the complete data processing process.

---

## 🧪 Testing

**File:** `test_arxiv_api.py`

A test script is included to verify the interaction with the arXiv API before running the complete workflow.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Pipeline development |
| Pandas | Data processing |
| arXiv API | Data source |
| Apache Parquet | Data storage |
| DuckDB | Analytical database |
| SQL | Data analytics |

---

## 📊 Results

The pipeline successfully processed:

### **9,950 research papers**

The processed data was:

- Extracted from the arXiv API
- Cleaned
- Validated
- Transformed
- Stored in Parquet
- Loaded into DuckDB
- Analyzed using SQL

The final pipeline execution completed successfully.

---

## 📁 Project Structure

```text
arxiv-data-engineering/
│
├── fetch_papers.py
├── clean_data.py
├── data_quality.py
├── to_parquet.py
├── transform_data.py
├── load_transformed.py
├── duckdb_analysis.py
├── pipeline.py
├── test_arxiv_api.py
│
├── papers.csv
├── papers_clean.csv
├── papers_clean.parquet
├── papers_transformed.parquet
└── papers.duckdb
```

---

## 🚀 How to Run

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pandas duckdb pyarrow requests
```

### 4. Run the complete pipeline

```bash
python pipeline.py
```

A successful execution should end with:

```text
PIPELINE COMPLETED SUCCESSFULLY
```

---

## 🎯 Data Engineering Concepts Demonstrated

This project demonstrates practical implementation of:

- API-based data ingestion
- ETL pipeline design
- Data cleaning
- Data quality validation
- Data transformation
- Columnar data storage
- Analytical database design
- SQL analytics
- Pipeline automation
- Reproducible data workflows

---

## 💡 Key Takeaway

The main objective of this project was to demonstrate the complete journey of data:

**From raw external source → to clean and validated data → to transformed analytical data → to database → to meaningful SQL insights.**

The project focuses on building a structured and reproducible data engineering workflow rather than simply collecting and analyzing data.

---

## 🔮 Future Improvements

Possible extensions to the current implementation include:

- Incremental data ingestion
- Scheduled pipeline execution
- Cloud object storage
- Apache Airflow orchestration
- Apache Spark processing
- Data lineage and observability
- Automated data quality reporting
- CI/CD integration

---

## 👤 Author

**Ibrahim Abdulaziz Alarifi**

Data Science — Artificial Intelligence

---

## 🤝 Program

Developed as part of the **Entropy Job Shadowing Program**.

---

## 📄 License

This project is intended for educational and portfolio purposes.