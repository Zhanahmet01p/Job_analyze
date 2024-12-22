import React, { useEffect, useState } from "react";

const Job = () => {
  const [vacancies, setVacancies] = useState([]);

  useEffect(() => {
    // Получаем данные с API
    fetch("http://localhost:5000/api/statistics")
      .then((response) => response.json())
      .then((data) => setVacancies(data));
  }, []);

  return (
    <div>
      <h1>Список вакансий</h1>
      <table>
        <thead>
          <tr>
            <th>Название вакансии</th>
            <th>Компания</th>
            <th>Зарплата</th>
            <th>Город</th>
            <th>Опыт</th>
            <th>Профессиональные роли</th>
            <th>Требуется письмо</th>
            <th>График работы</th>
          </tr>
        </thead>
        <tbody>
          {vacancies.map((vacancy, index) => (
            <tr key={index}>
              <td>{vacancy.name}</td>
              <td>{vacancy.employer}</td>
              <td>{vacancy.salary_from}</td>
              <td>{vacancy.area_name}</td>
              <td>{vacancy.experience_years} лет</td>
              <td>{vacancy.professional_roles}</td>
              <td>{vacancy.response_letter_required ? "Да" : "Нет"}</td>
              <td>{vacancy.schedule}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Job;
