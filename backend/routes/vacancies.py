from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np

vacancies_bp = Blueprint("vacancies", __name__)

def register_vacancy_routes(app, df):
    @vacancies_bp.route("/api/vacancies", methods=['GET'])
    def get_vacancies():
        # Добавляем пагинацию
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 50, type=int)
        
        start = (page - 1) * per_page
        end = start + per_page
        
        # Преобразуем DataFrame в список словарей с нужными полями
        vacancies = []
        for idx, row in df.iloc[start:end].iterrows():
            # Безопасно получаем значения
            salary_from = row.get('salary_from')
            if pd.isna(salary_from):
                salary_from = None
            else:
                try:
                    salary_from = float(salary_from)
                except:
                    salary_from = None
            
            employer_name = row.get('employer_name')
            if pd.isna(employer_name):
                employer_name = "Не указано"
            
            experience_years = row.get('experience_years', 0)
            if pd.isna(experience_years):
                experience_years = 0
            else:
                try:
                    experience_years = int(experience_years)
                except:
                    experience_years = 0
            
            currency = row.get('currency')
            if pd.isna(currency):
                currency = 'RUR'
            
            area = row.get('area_name')
            if pd.isna(area):
                area = "Не указано"
            
            vacancy = {
                'id': idx,
                'name': row.get('name', 'Без названия'),
                'employer': {
                    'name': employer_name
                },
                'salary_from': salary_from,
                'currency': currency,
                'experience_years': experience_years,
                'experience_text': row.get('experience_text', 'Не указано'),
                'area': area
            }
            vacancies.append(vacancy)
        
        return jsonify({
            'vacancies': vacancies,
            'total': len(df),
            'page': page,
            'per_page': per_page,
            'total_pages': (len(df) + per_page - 1) // per_page
        })

    @vacancies_bp.route("/api/search", methods=['GET'])
    def search():
        query = request.args.get("query", "").strip().lower()
        
        if not query or len(query) < 2:
            return jsonify([])
        
        # Поиск по названию вакансии
        mask = df['name'].str.lower().str.contains(query, na=False)
        results = df[mask].head(50)  # Ограничиваем результаты
        
        # Преобразуем результаты
        vacancies = []
        for idx, row in results.iterrows():
            salary_from = row.get('salary_from')
            if pd.isna(salary_from):
                salary_from = None
            else:
                try:
                    salary_from = float(salary_from)
                except:
                    salary_from = None
            
            vacancy = {
                'id': idx,
                'name': row.get('name', 'Без названия'),
                'employer': {
                    'name': row.get('employer_name', 'Не указано')
                },
                'salary_from': salary_from,
                'currency': row.get('currency', 'RUR'),
                'experience_years': int(row.get('experience_years', 0)) if not pd.isna(row.get('experience_years', 0)) else 0,
                'area': row.get('area_name', 'Не указано')
            }
            vacancies.append(vacancy)
        
        return jsonify(vacancies)

    @vacancies_bp.route("/api/vacancy/<int:vacancy_id>", methods=['GET'])
    def get_vacancy(vacancy_id):
        try:
            if vacancy_id >= len(df):
                return jsonify({'error': 'Vacancy not found'}), 404
            
            row = df.iloc[vacancy_id]
            
            salary_from = row.get('salary_from')
            if pd.isna(salary_from):
                salary_from = None
            else:
                try:
                    salary_from = float(salary_from)
                except:
                    salary_from = None
            
            salary_to = row.get('salary_to')
            if pd.isna(salary_to):
                salary_to = None
            else:
                try:
                    salary_to = float(salary_to)
                except:
                    salary_to = None
            
            return jsonify({
                'id': vacancy_id,
                'name': row.get('name', 'Без названия'),
                'employer': {
                    'name': row.get('employer_name', 'Не указано')
                },
                'salary_from': salary_from,
                'salary_to': salary_to,
                'currency': row.get('currency', 'RUR'),
                'experience_years': int(row.get('experience_years', 0)) if not pd.isna(row.get('experience_years', 0)) else 0,
                'experience_text': row.get('experience_text', 'Не указано'),
                'area': row.get('area_name', 'Не указано'),
                'description': row.get('description', 'Описание отсутствует')
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    app.register_blueprint(vacancies_bp)