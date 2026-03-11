from flask import Flask
from flask_cors import CORS

from services.preprocessing import preprocess_data
from routes.vacancies import register_vacancy_routes
from routes.analytics import register_analytics_routes

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для всех маршрутов

print("=" * 50)
print("Loading dataset...")
print("=" * 50)

try:
    df = preprocess_data()
    print(f"Dataset loaded successfully: {len(df)} vacancies")
    print(f"Columns: {df.columns.tolist()}")
    print("=" * 50)
except Exception as e:
    print(f"Error loading dataset: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Регистрируем маршруты
register_vacancy_routes(app, df)
register_analytics_routes(app, df)

print("🚀 Routes registered:")
print("  - GET /api/vacancies")
print("  - GET /api/search?query=...")
print("  - GET /api/vacancy/<id>")
print("  - GET /api/analytics/salary")
print("  - GET /api/analytics/cities")
print("  - GET /api/analytics/experience")
print("  - GET /api/analytics/salary_range")
print("  - GET /api/analytics/dashboard")
print("=" * 50)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)