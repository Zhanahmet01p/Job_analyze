from pathlib import Path
import requests
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

URL = "https://api.hh.ru/vacancies"

params = {
    "text": "developer",
    "area": 159,
    "per_page": 100,
    "page": 0
}

vacancies = []

for page in range(10):
    params["page"] = page

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break

    data = response.json()
    vacancies.extend(data.get("items", []))

    if len(data.get("items", [])) < 100:
        break

df = pd.DataFrame(vacancies)

file_path = DATA_DIR / "vacancies.csv"

df.to_csv(file_path, index=False, encoding="utf-8-sig")

print(f"Data saved to {file_path}")