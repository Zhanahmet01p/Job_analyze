import pandas as pd

# Функция для загрузки и предобработки данных
def preprocess_data():
    # Загружаем данные
    df = pd.read_csv('.././data/vacancies.csv')

    # Очистка данных (удаляем строки с пропущенными значениями)
    df = df.dropna(subset=['salary', 'area', 'experience', 'professional_roles'])

    # Преобразуем зарплаты в числовой формат
    df['salary_from'] = df['salary'].apply(lambda x: eval(x).get('from') if isinstance(x, str) else None)
    df['salary_to'] = df['salary'].apply(lambda x: eval(x).get('to') if isinstance(x, str) else None)
    df['currency'] = df['salary'].apply(lambda x: eval(x).get('currency') if isinstance(x, str) else None)

    # Преобразуем опыт работы в числа (например, "более 6 лет" в 7)
    df['experience_years'] = df['experience'].apply(lambda x: extract_experience(x))

    # Преобразуем местоположение в текст
    df['area_name'] = df['area'].apply(lambda x: eval(x).get('name') if isinstance(x, str) else None)

    return df

# Функция для извлечения опыта работы
def extract_experience(experience):
    if 'более 6 лет' in experience:
        return 7
    if 'от 3 до 6 лет' in experience:
        return 5
    if 'от 1 года до 3 лет' in experience:
        return 2
    return 0
