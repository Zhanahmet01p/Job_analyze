from flask import Flask, jsonify
from models.statistics import get_full_vacancy_info
from models.preprocessing import preprocess_data

app = Flask(__name__)

# Роут для получения статистики
@app.route('/api/statistics', methods=['GET'])
def statistics():
    # Предобработка данных
    df = preprocess_data()

    # Получаем статистику по вакансиям
    full_vacancy_info = get_full_vacancy_info(df)

    return jsonify(full_vacancy_info)

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
