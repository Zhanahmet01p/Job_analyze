import React, { useState } from "react";

const FilterPanel = ({ onFilterChange }) => {
  const [company, setCompany] = useState("");
  const [minSalary, setMinSalary] = useState("");

  const handleFilterChange = () => {
    onFilterChange({
      company,
      minSalary: parseInt(minSalary, 10) || 0,
    });
  };

  return (
    <div className="bg-white p-4 rounded shadow mb-6">
      <h2 className="text-xl font-semibold mb-4 text-gray-700">Фильтры</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <input
          type="text"
          placeholder="Компания"
          className="border p-2 rounded w-full"
          value={company}
          onChange={(e) => setCompany(e.target.value)}
        />
        <input
          type="number"
          placeholder="Минимальная зарплата"
          className="border p-2 rounded w-full"
          value={minSalary}
          onChange={(e) => setMinSalary(e.target.value)}
        />
      </div>
      <button
        className="mt-4 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        onClick={handleFilterChange}
      >
        Применить фильтры
      </button>
    </div>
  );
};

export default FilterPanel;
