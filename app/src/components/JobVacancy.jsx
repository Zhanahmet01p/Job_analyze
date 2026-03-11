import React from "react";

const JobVacancyList = ({ vacancies }) => {
  if (!vacancies || vacancies.length === 0) {
    return (
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">
          Список вакансий
        </h2>
        <p className="text-gray-500 text-center py-8">
          Нет вакансий для отображения
        </p>
      </div>
    );
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-4 text-gray-700">
        Список вакансий ({vacancies.length})
      </h2>
      <div className="space-y-4">
        {vacancies.map((vacancy, index) => (
          <div
            key={vacancy.id || index}
            className="border rounded-lg p-4 hover:shadow-md transition-shadow"
          >
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              {vacancy.name}
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm">
              <p className="text-gray-600">
                <span className="font-medium">Компания:</span>{" "}
                {vacancy.employer?.name || "Не указано"}
              </p>
              <p className="text-gray-600">
                <span className="font-medium">Зарплата:</span>{" "}
                {vacancy.salary_from ? (
                  <>
                    {vacancy.salary_from.toLocaleString()} {vacancy.currency || "руб."}
                  </>
                ) : (
                  "Не указана"
                )}
              </p>
              <p className="text-gray-600">
                <span className="font-medium">Опыт:</span>{" "}
                {vacancy.experience_years === 0 && "Нет опыта"}
                {vacancy.experience_years === 1 && "До 1 года"}
                {vacancy.experience_years === 2 && "1-3 года"}
                {vacancy.experience_years === 5 && "3-6 лет"}
                {vacancy.experience_years === 7 && "Более 6 лет"}
              </p>
              <p className="text-gray-600">
                <span className="font-medium">Город:</span>{" "}
                {vacancy.area || "Не указан"}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default JobVacancyList;