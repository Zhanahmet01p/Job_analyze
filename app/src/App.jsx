import  { useState, useEffect } from "react";
import JobVacancyList from "./components/JobVacancy";
import FilterPanel from "./components/Filter";
import ChartVisualization from "./components/Chart";

import "./index.scss";

const App = () => {
  const [vacancies, setVacancies] = useState([]);
  const [filteredVacancies, setFilteredVacancies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchVacancies();
  }, []);

  const fetchVacancies = async () => {
    try {
      setLoading(true);
      const response = await fetch("http://localhost:5000/api/vacancies");
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      // Предполагаем, что API возвращает объект с полем vacancies
      const vacanciesList = data.vacancies || data;
      setVacancies(vacanciesList);
      setFilteredVacancies(vacanciesList);
      setError(null);
    } catch (error) {
      console.error("Data upload error:", error);
      setError("Failed to load data. Please check your connection to the server.");
    } finally {
      setLoading(false);
    }
  };

  const applyFilters = (filters) => {
    if (!vacancies.length) return;

    let filtered = [...vacancies];

    // Фильтр по поисковому запросу
    if (filters.searchQuery) {
      filtered = filtered.filter((vacancy) =>
        vacancy.name?.toLowerCase().includes(filters.searchQuery.toLowerCase())
      );
    }

    // Фильтр по компании
    if (filters.company) {
      filtered = filtered.filter((vacancy) =>
        vacancy.employer?.name?.toLowerCase().includes(filters.company.toLowerCase())
      );
    }

    // Фильтр по минимальной зарплате
    if (filters.minSalary && filters.minSalary > 0) {
      filtered = filtered.filter(
        (vacancy) => vacancy.salary_from && vacancy.salary_from >= filters.minSalary
      );
    }

    // Фильтр по опыту
    if (filters.experience && filters.experience !== 'all') {
      filtered = filtered.filter(
        (vacancy) => vacancy.experience_years === parseInt(filters.experience)
      );
    }

    setFilteredVacancies(filtered);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-700 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading data...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 mb-4">{error}</p>
          <button
            onClick={fetchVacancies}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <h1 className="text-3xl font-bold text-center text-blue-700 mb-6">
        Job Vacancy Analysis
      </h1>
      <div className="max-w-6xl mx-auto">
        <FilterPanel 
          onFilterChange={applyFilters} 
          totalVacancies={vacancies.length}
        />
        <ChartVisualization vacancies={filteredVacancies} />
        <JobVacancyList vacancies={filteredVacancies} />
      </div>
    </div>
  );
};

export default App;