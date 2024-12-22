import requests
import pandas as pd

URL = "https://api.hh.ru/vacancies"

params = {
    "text": "developer",  
    "area": 159,          
    "per_page": 100,    
    "page": 0             
}

vacancies = []


for page in range(10): 
    params['page'] = page
    response = requests.get(URL, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break
    data = response.json()
    vacancies.extend(data.get('items', []))
    if len(data.get('items', [])) < 100:
        break  

df = pd.DataFrame(vacancies)

df.to_csv("../data/vacancies.csv", index=False, encoding="utf-8-sig")
print("Данные сохранены в файл vacancies.csv")
