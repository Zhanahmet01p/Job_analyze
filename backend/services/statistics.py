import pandas as pd
import numpy as np

def get_salary_stats(df):
    # Фильтруем только валидные зарплаты
    salary_df = df.dropna(subset=["salary_from"])
    salary_df = salary_df[salary_df["salary_from"] > 0]
    
    if len(salary_df) == 0:
        return {
            "average_salary": 0,
            "median_salary": 0,
            "max_salary": 0,
            "min_salary": 0,
            "total_with_salary": 0
        }
    
    return {
        "average_salary": float(salary_df["salary_from"].mean()),
        "median_salary": float(salary_df["salary_from"].median()),
        "max_salary": float(salary_df["salary_from"].max()),
        "min_salary": float(salary_df["salary_from"].min()),
        "total_with_salary": len(salary_df)
    }


def get_top_cities(df, limit=10):
    city_counts = df["area_name"].value_counts().head(limit)
    
    result = {}
    for city, count in city_counts.items():
        if pd.notna(city) and city != "Не указано":
            result[str(city)] = int(count)
    
    return result


def get_experience_distribution(df):
    exp_counts = df["experience_years"].value_counts().sort_index()
    
    # Преобразуем в удобный формат
    result = []
    for years, count in exp_counts.items():
        if pd.notna(years):
            # Определяем текстовое представление
            if years == 0:
                exp_text = "Нет опыта"
            elif years == 1:
                exp_text = "До 1 года"
            elif years == 2:
                exp_text = "1-3 года"
            elif years == 5:
                exp_text = "3-6 лет"
            elif years == 7:
                exp_text = "Более 6 лет"
            else:
                exp_text = f"{int(years)} лет"
            
            result.append({
                "years": int(years),
                "text": exp_text,
                "count": int(count)
            })
    
    return result


def get_salary_by_experience(df):
    """Получить статистику зарплат по уровням опыта"""
    salary_df = df.dropna(subset=["salary_from"])
    salary_df = salary_df[salary_df["salary_from"] > 0]
    
    result = {}
    for years in [0, 1, 2, 5, 7]:
        exp_df = salary_df[salary_df["experience_years"] == years]
        if len(exp_df) > 0:
            if years == 0:
                exp_text = "Нет опыта"
            elif years == 1:
                exp_text = "До 1 года"
            elif years == 2:
                exp_text = "1-3 года"
            elif years == 5:
                exp_text = "3-6 лет"
            elif years == 7:
                exp_text = "Более 6 лет"
            
            result[exp_text] = {
                "avg": float(exp_df["salary_from"].mean()),
                "median": float(exp_df["salary_from"].median()),
                "min": float(exp_df["salary_from"].min()),
                "max": float(exp_df["salary_from"].max()),
                "count": len(exp_df)
            }
    
    return result