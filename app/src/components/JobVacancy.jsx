import React from "react";

const JobVacancyList = ({ vacancies }) => {
  if (!vacancies || vacancies.length === 0) {
    return (
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">
          List of vacancies
        </h2>
        <p className="text-gray-500 text-center py-8">
          No vacancies to display
        </p>
      </div>
    );
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-4 text-gray-700">
        List of vacancies ({vacancies.length})
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
                <span className="font-medium">Company:</span>{" "}
                {vacancy.employer?.name || "Not specified"}
              </p>
              <p className="text-gray-600">
                <span className="font-medium">Salary:</span>{" "}
                {vacancy.salary_from ? (
                  <>
                    {vacancy.salary_from.toLocaleString()} {vacancy.currency || "руб."}
                  </>
                ) : (
                  "Not specified"
                )}
              </p>
              <p className="text-gray-600">
                <span className="font-medium">Experience:</span>{" "}
                {vacancy.experience_years === 0 && "No experience"}
                {vacancy.experience_years === 1 && "Less than 1 year"}
                {vacancy.experience_years === 2 && "1-3 years"}
                {vacancy.experience_years === 5 && "3-6 years"}
                {vacancy.experience_years === 7 && "More than 6 years"}
              </p>
              <p className="text-gray-600">
                <span className="font-medium">City:</span>{" "}
                {vacancy.area || "Not specified"}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default JobVacancyList;