from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np
from services.statistics import (
    get_salary_stats,
    get_top_cities,
    get_experience_distribution,
    get_salary_by_experience
)

analytics_bp = Blueprint("analytics", __name__)

def register_analytics_routes(app, df):
    @analytics_bp.route("/api/analytics/salary", methods=['GET'])
    def salary():
        try:
            stats = get_salary_stats(df)
            by_experience = get_salary_by_experience(df)
            
            return jsonify({
                "stats": stats,
                "by_experience": by_experience
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @analytics_bp.route("/api/analytics/cities", methods=['GET'])
    def cities():
        try:
            limit = request.args.get('limit', 10, type=int)
            city_stats = get_top_cities(df, limit)
            
            # Преобразуем в список для удобства
            cities_list = [{"name": k, "count": v} for k, v in city_stats.items()]
            
            return jsonify({
                "cities": cities_list,
                "total": len(cities_list)
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @analytics_bp.route("/api/analytics/experience", methods=['GET'])
    def experience():
        try:
            exp_dist = get_experience_distribution(df)
            return jsonify(exp_dist)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @analytics_bp.route("/api/analytics/salary_range", methods=['GET'])
    def salary_range():
        """Распределение зарплат по диапазонам"""
        try:
            salary_df = df.dropna(subset=["salary_from"])
            salary_df = salary_df[salary_df["salary_from"] > 0]
            
            if len(salary_df) == 0:
                return jsonify({"ranges": [], "counts": []})
            
            # Создаем диапазоны
            bins = [0, 30000, 50000, 70000, 100000, 150000, 200000, float('inf')]
            labels = ['до 30k', '30k-50k', '50k-70k', '70k-100k', '100k-150k', '150k-200k', '200k+']
            
            salary_df_copy = salary_df.copy()
            salary_df_copy['salary_range'] = pd.cut(salary_df_copy['salary_from'], bins=bins, labels=labels)
            distribution = salary_df_copy['salary_range'].value_counts().sort_index()
            
            return jsonify({
                "ranges": distribution.index.tolist(),
                "counts": distribution.values.tolist()
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @analytics_bp.route("/api/analytics/dashboard", methods=['GET'])
    def dashboard():
        """Получить все данные для дашборда одним запросом"""
        try:
            return jsonify({
                "salary_stats": get_salary_stats(df),
                "top_cities": get_top_cities(df, 5),
                "experience_distribution": get_experience_distribution(df),
                "total_vacancies": len(df)
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    app.register_blueprint(analytics_bp)