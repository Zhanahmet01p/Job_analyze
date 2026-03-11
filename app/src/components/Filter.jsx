import React, { useState } from "react";

const FilterPanel = ({ onFilterChange, totalVacancies }) => {
  const [company, setCompany] = useState("");
  const [minSalary, setMinSalary] = useState("");
  const [experience, setExperience] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");

  const handleFilterChange = () => {
    onFilterChange({
      company: company.trim(),
      minSalary: minSalary ? parseInt(minSalary, 10) : 0,
      experience: experience,
      searchQuery: searchQuery.trim()
    });
  };

  const handleReset = () => {
    setCompany("");
    setMinSalary("");
    setExperience("all");
    setSearchQuery("");
    onFilterChange({});
  };

  return (
    <div className="bg-white p-4 rounded shadow mb-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-semibold text-gray-700">Filters</h2>
        <span className="text-sm text-gray-500">
          Total vacancies: {totalVacancies}
        </span>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <input
          type="text"
          placeholder="Name search"
          className="border p-2 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-300"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        
        <input
          type="text"
          placeholder="Company name"
          className="border p-2 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-300"
          value={company}
          onChange={(e) => setCompany(e.target.value)}
        />
        
        <input
          type="number"
          placeholder="Min. salary"
          className="border p-2 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-300"
          value={minSalary}
          onChange={(e) => setMinSalary(e.target.value)}
          min="0"
          step="1000"
        />
        
        <select
          className="border p-2 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-300"
          value={experience}
          onChange={(e) => setExperience(e.target.value)}
        >
          <option value="all">Any experience</option>
          <option value="0">No experience</option>
          <option value="1">Less than 1 year</option>
          <option value="2">1-3 years</option>
          <option value="5">3-6 years</option>
          <option value="7">More than 6 years</option>
        </select>
      </div>
      
      <div className="mt-4 flex gap-2">
        <button
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition-colors"
          onClick={handleFilterChange}
        >
          Apply filters
        </button>
        <button
          className="bg-gray-300 text-gray-700 px-6 py-2 rounded hover:bg-gray-400 transition-colors"
          onClick={handleReset}
        >
          Reset
        </button>
      </div>
    </div>
  );
};

export default FilterPanel;