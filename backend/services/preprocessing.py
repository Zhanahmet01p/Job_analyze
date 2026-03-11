import pandas as pd
import os
import ast
import json

def preprocess_data():
    # Определяем путь к файлу относительно текущего скрипта
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Поднимаемся на два уровня вверх (из backend/services/ в корень проекта)
    project_root = os.path.dirname(os.path.dirname(current_dir))
    
    # Пробуем разные пути
    possible_paths = [
        os.path.join(project_root, 'data', 'vacancies.csv'),
        os.path.join(project_root, 'backend', 'data', 'vacancies.csv'),
        os.path.join(current_dir, '..', 'data', 'vacancies.csv'),
        '../data/vacancies.csv',
        'data/vacancies.csv'
    ]
    
    df = None
    for path in possible_paths:
        try:
            print(f"Trying path: {path}")
            if os.path.exists(path):
                df = pd.read_csv(path)
                print(f"Successfully loaded from: {path}")
                print(f"Columns in dataset: {df.columns.tolist()}")
                break
        except Exception as e:
            print(f"Failed to load from {path}: {e}")
            continue
    
    if df is None:
        raise FileNotFoundError(
            f"Could not find vacancies.csv. Tried: {possible_paths}\n"
            f"Current directory: {os.getcwd()}\n"
            f"Script directory: {current_dir}"
        )

    # Безопасное преобразование строк в словари
    def safe_parse_json(json_str, field_name=None):
        if pd.isna(json_str) or not isinstance(json_str, str):
            return None if field_name else {}
        try:
            # Пробуем распарсить как JSON или Python dict
            if json_str.strip().startswith('{'):
                parsed = ast.literal_eval(json_str)
            else:
                parsed = json.loads(json_str)
            
            if field_name:
                return parsed.get(field_name)
            return parsed
        except:
            try:
                # Если не получилось, пробуем просто JSON
                parsed = json.loads(json_str.replace("'", '"'))
                if field_name:
                    return parsed.get(field_name)
                return parsed
            except:
                return None if field_name else {}

    # Извлекаем информацию о зарплате
    df['salary_from'] = df['salary'].apply(lambda x: safe_parse_json(x, 'from'))
    df['salary_to'] = df['salary'].apply(lambda x: safe_parse_json(x, 'to'))
    df['currency'] = df['salary'].apply(lambda x: safe_parse_json(x, 'currency'))
    
    # Извлекаем информацию о местоположении
    df['area_name'] = df['area'].apply(lambda x: safe_parse_json(x, 'name'))
    
    # Извлекаем информацию о работодателе
    df['employer_name'] = df['employer'].apply(lambda x: safe_parse_json(x, 'name'))
    
    # Извлекаем опыт
    df['experience_years'] = df['experience'].apply(extract_experience)
    
    # Создаем понятное название для опыта
    df['experience_text'] = df['experience_years'].apply(experience_to_text)
    
    # Удаляем строки с критическими пропусками
    df = df.dropna(subset=['name'])  # Название вакансии обязательно
    
    print(f"Preprocessed {len(df)} vacancies")
    print(f"Sample salary_from: {df['salary_from'].head(3).tolist()}")
    print(f"Sample employer_name: {df['employer_name'].head(3).tolist()}")
    
    return df

def extract_experience(experience):
    if pd.isna(experience) or not isinstance(experience, str):
        return 0
    
    experience = experience.lower()
    if 'более 6 лет' in experience or 'more than 6' in experience:
        return 7
    if 'от 3 до 6 лет' in experience or '3 to 6' in experience:
        return 5
    if 'от 1 года до 3 лет' in experience or '1 to 3' in experience:
        return 2
    if 'нет опыта' in experience or 'no experience' in experience:
        return 0
    return 1  # По умолчанию

def experience_to_text(years):
    if years == 0:
        return "Нет опыта"
    elif years == 1:
        return "До 1 года"
    elif years == 2:
        return "1-3 года"
    elif years == 5:
        return "3-6 лет"
    elif years == 7:
        return "Более 6 лет"
    else:
        return f"{years} лет"