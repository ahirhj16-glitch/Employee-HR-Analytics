
SELECT Department,round(AVG(Salary),2) AS Avrage_Department_Salary
FROM employees
GROUP BY Department;

SELECT Job_Role,round(AVG(Salary),2) AS Avrage_Job_Role_Salary
FROM employees
GROUP BY Job_Role;

SELECT Department,round(sum(Salary),2) AS Total_Department_Salary
FROM employees
GROUP BY Department;

SELECT Job_Role,round(sum(Salary),2) AS Toatal_Job_Role_Salary
FROM employees
GROUP BY Job_Role;

SELECT City,round(AVG(Salary),2) AS Avrage_City_Salary
FROM employees
GROUP BY City;

SELECT City,round(sum(Salary),2) AS Total_City_Salary
FROM employees
GROUP BY City;

select Experience_Years,round(sum(Salary),2) as Experince_slary
from employees
group by Experience_Years;

SELECT City, COUNT(*) AS Total_Employees
FROM employees
GROUP BY City;

SELECT
    Department,
    Performance,
    COUNT(*) AS Total_Employees
FROM employees
GROUP BY Department, Performance
ORDER BY Department, Performance;

SELECT
    Job_Role,
    Performance,
    COUNT(*) AS Total_Employees
FROM employees
GROUP BY Job_Role, Performance
ORDER BY Job_Role, Performance;

SELECT
    Department,
    COUNT(*) AS Total_Employees
FROM employees
GROUP BY Department
ORDER BY Total_Employees DESC;

SELECT
    Experience_Years,
    ROUND(AVG(Salary), 2) AS Average_Salary
FROM employees
GROUP BY Experience_Years
ORDER BY Experience_Years;