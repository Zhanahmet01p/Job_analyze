import React, { useState, useEffect } from "react";
import JobVacancyList from "./components/JobVacancy";
import FilterPanel from "./components/Filter";
import ChartVisualization from "./components/Chart";

import "./index.scss";

const App = () => {
  const [vacancies, setVacancies] = useState([]);
  const [filteredVacancies, setFilteredVacancies] = useState([]);
  const [filters, setFilters] = useState({});

  useEffect(() => {
    fetch("http://localhost:5000/api/statistics")
      .then((response) => response.json())
      .then((data) => {
        setVacancies(data);
        setFilteredVacancies(data);
      })
      .catch((error) => console.error("Ошибка загрузки данных:", error));
  }, []);

  const applyFilters = (filters) => {
    let filtered = vacancies;

    if (filters.company) {
      filtered = filtered.filter((vacancy) =>
        vacancy.company.toLowerCase().includes(filters.company.toLowerCase())
      );
    }

    if (filters.minSalary) {
      filtered = filtered.filter(
        (vacancy) => vacancy.salary >= filters.minSalary
      );
    }

    setFilteredVacancies(filtered);
    setFilters(filters);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <h1 className="text-3xl font-bold text-center text-blue-700 mb-6">
        Анализ вакансий
      </h1>
      <div className="max-w-6xl mx-auto">
        <FilterPanel onFilterChange={applyFilters} />
        <ChartVisualization vacancies={filteredVacancies} />
        <JobVacancyList vacancies={filteredVacancies} />
      </div>
    </div>
  );
};

export default App;
