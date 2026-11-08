import subprocess
import sys


def run_step(script_name):
    print(f"\n{'=' * 60}")
    print(f"Running: {script_name}")
    print(f"{'=' * 60}")

    result = subprocess.run(
        [sys.executable, script_name],
        check=True
    )

    print(f"Completed: {script_name}")
    return result


def main():
    steps = [
        "clean_data.py",
        "to_parquet.py",
        "data_quality.py",
        "transform_data.py",
        "load_transformed.py",
        "duckdb_analysis.py",
    ]

    for step in steps:
        run_step(step)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()