import pandas as pd

# Функция для получения подробной статистики по вакансиям
def get_full_vacancy_info(df):
    vacancy_details = df[['name', 'employer', 'salary_from', 'area_name', 'experience_years', 'professional_roles', 'response_letter_required', 'working_time_modes', 'employment', 'schedule']]

    # Преобразуем зарплату, если она пустая
    vacancy_details['salary_from'] = vacancy_details['salary_from'].fillna('Не указана')

    # Преобразуем опыт работы, если он пустой
    vacancy_details['experience_years'] = vacancy_details['experience_years'].fillna('Не указано')

    # Преобразуем профессиональные роли
    vacancy_details['professional_roles'] = vacancy_details['professional_roles'].fillna('Не указаны')

    return vacancy_details.to_dict(orient='records')
