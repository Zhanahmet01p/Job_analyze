import React from "react";

const JobVacancyList = ({ vacancies }) => {
  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-4 text-gray-700">
        Список вакансий
      </h2>
      {vacancies.map((vacancy) => (
        <div
          key={vacancy.id}
          className="border-b last:border-0 py-4 flex flex-col gap-2"
        >
          <h3 className="text-lg font-bold text-gray-800">{vacancy.name}</h3>
          <p className="text-gray-600">
            <strong>Компания:</strong> {vacancy.employer.name}
          </p>
          <p className="text-gray-600">
            <strong>Зарплата:</strong> {vacancy.salary_from} {vacancy.currency}
          </p>
          <p className="text-gray-600">
            <strong>Требуемый опыт:</strong> {vacancy.experience_years}
          </p>
        </div>
      ))}
    </div>
  );
};

export default JobVacancyList;
