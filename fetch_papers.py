import requests
import xml.etree.ElementTree as ET
import csv
import time

URL = "https://export.arxiv.org/api/query"

CATEGORIES = [
    "cs.DS",
    "cs.DM",
    "cs.CC",
    "cs.CG"
]

TARGET_PAPERS = 10000
BATCH_SIZE = 100

all_papers = []

for category in CATEGORIES:

    print(f"\nFetching category: {category}")

    start = 0

    while len(all_papers) < TARGET_PAPERS:

        params = {
            "search_query": f"cat:{category}",
            "start": start,
            "max_results": BATCH_SIZE,
        }

        response = requests.get(
            URL,
            params=params,
            timeout=30
        )

        print(
            f"{category} | start={start} | status={response.status_code}"
        )

        root = ET.fromstring(response.text)

        namespace = {
            "atom": "http://www.w3.org/2005/Atom"
        }

        entries = root.findall("atom:entry", namespace)

        if not entries:
            break

        for entry in entries:

            paper_id = entry.find(
                "atom:id",
                namespace
            ).text

            title = entry.find(
                "atom:title",
                namespace
            ).text.strip()

            published = entry.find(
                "atom:published",
                namespace
            ).text

            all_papers.append([
                paper_id,
                title,
                published,
                category
            ])

        start += BATCH_SIZE

        print(f"Total collected: {len(all_papers)}")

        time.sleep(3)

        if len(entries) < BATCH_SIZE:
            break


# Remove duplicate papers
unique_papers = {}

for paper in all_papers:
    unique_papers[paper[0]] = paper

all_papers = list(unique_papers.values())


# Save to CSV
with open(
    "papers.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "paper_id",
        "title",
        "published",
        "category"
    ])

    writer.writerows(all_papers)


print("\nDONE!")
print(f"Unique papers saved: {len(all_papers)}")
print("File: papers.csv")