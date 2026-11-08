import requests
import xml.etree.ElementTree as ET

url = "https://export.arxiv.org/api/query"

params = {
    "search_query": "cat:cs.DS AND submittedDate:[202606010000 TO 202606302359]",
    "start": 0,
    "max_results": 2000,
}

response = requests.get(url, params=params, timeout=30)

print("Status code:", response.status_code)

root = ET.fromstring(response.text)

namespace = {"atom": "http://www.w3.org/2005/Atom"}

entries = root.findall("atom:entry", namespace)



print(f"Number of papers: {len(entries)}")
print()

for entry in entries:
    paper_id = entry.find("atom:id", namespace).text
    title = entry.find("atom:title", namespace).text.strip()
    published = entry.find("atom:published", namespace).text

    print("ID:", paper_id)
    print("Title:", title)
    print("Published:", published)
    print("-" * 60)