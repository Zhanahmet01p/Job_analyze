import React, { useState, useEffect } from 'react';

const ChartVisualization = ({ vacancies }) => {
  const [chartType, setChartType] = useState('salary');
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    if (!vacancies || vacancies.length === 0) return;

    if (chartType === 'salary') {
      // Группировка зарплат по диапазонам
      const ranges = {
        'до 30k': 0,
        '30k-50k': 0,
        '50k-70k': 0,
        '70k-100k': 0,
        '100k-150k': 0,
        '150k-200k': 0,
        '200k+': 0
      };

      vacancies.forEach(v => {
        const salary = v.salary_from;
        if (!salary) return;
        
        if (salary < 30000) ranges['до 30k']++;
        else if (salary < 50000) ranges['30k-50k']++;
        else if (salary < 70000) ranges['50k-70k']++;
        else if (salary < 100000) ranges['70k-100k']++;
        else if (salary < 150000) ranges['100k-150k']++;
        else if (salary < 200000) ranges['150k-200k']++;
        else ranges['200k+']++;
      });

      setChartData({
        labels: Object.keys(ranges),
        values: Object.values(ranges),
        title: 'Salary distribution'
      });
    } else if (chartType === 'experience') {
      // Распределение по опыту
      const expCounts = {
        'No experience': 0,
        'Less than 1 year': 0,
        '1-3 years': 0,
        '3-6 years': 0,
        'More than 6 years': 0
      };

      vacancies.forEach(v => {
        const exp = v.experience_years;
        if (exp === 0) expCounts['No experience']++;
        else if (exp === 1) expCounts['Less than 1 year']++;
        else if (exp === 2) expCounts['1-3 years']++;
        else if (exp === 5) expCounts['3-6 years']++;
        else if (exp === 7) expCounts['More than 6 years']++;
      });

      setChartData({
        labels: Object.keys(expCounts),
        values: Object.values(expCounts),
        title: 'Experience distribution'
      });
    }
  }, [vacancies, chartType]);

  if (!chartData || vacancies.length === 0) {
    return (
      <div className="bg-white p-4 rounded shadow mb-6">
        <p className="text-gray-500 text-center py-8">
          No data available for chart visualization
        </p>
      </div>
    );
  }

  // Простая визуализация в виде столбцов (без сторонних библиотек)
  const maxValue = Math.max(...chartData.values);

  return (
    <div className="bg-white p-4 rounded shadow mb-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-semibold text-gray-700">
          {chartData.title}
        </h2>
        <select
          className="border p-2 rounded"
          value={chartType}
          onChange={(e) => setChartType(e.target.value)}
        >
          <option value="salary">By salary</option>
          <option value="experience">By experience</option>
        </select>
      </div>

      <div className="space-y-2">
        {chartData.labels.map((label, index) => {
          const value = chartData.values[index];
          const percentage = maxValue > 0 ? (value / maxValue) * 100 : 0;
          
          return (
            <div key={label} className="flex items-center gap-2">
              <div className="w-24 text-sm text-gray-600">{label}:</div>
              <div className="flex-1 h-8 bg-gray-200 rounded overflow-hidden">
                <div
                  className="h-full bg-blue-500 flex items-center justify-end px-2 text-xs text-white"
                  style={{ width: `${percentage}%` }}
                >
                  {value > 0 && value}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ChartVisualization;