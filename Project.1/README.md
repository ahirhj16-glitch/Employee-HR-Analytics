## Project Overview

This project analyzes employee HR data using Python, Pandas, MySQL, and Matplotlib.

The main goals of this project are to analyze average employee salaries and understand employee performance across different cities, departments, and job roles.

This project also focuses on cleaning messy data, including inconsistent data types, duplicate records, and missing values.

## Tools & Technologies

- Python
- Pandas
- MySQL
- SQL
- SQLAlchemy
- Matplotlib
- CSV
- Data Cleaning
- Data Analysis
- Data Visualization

## Dataset

The dataset contains employee HR records with the following columns:

- Employee_ID
- Employee_Name
- Department
- Job_Role
- City
- Experience_Years
- Salary
- Performance
- Employment_Type
- Joining_Date

## Data Cleaning

The dataset contained several data quality issues, including:

- Missing salary values
- Missing city names
- Missing performance values
- Missing experience values
- Duplicate rows
- Inconsistent department names
- Inconsistent job role names
- Inconsistent city names
- Inconsistent employment type names
- Invalid salary values
- Invalid experience values

The data was cleaned using Python and Pandas before analysis.

## Important Data Cleaning Decisions

- The text value `"five"` in `Experience_Years` was converted to `5`.
- Negative salary values were treated as invalid.
- Negative experience values were treated as invalid.
- Text values in `Employment_Type`, `Job_Role`, `City`, and `Department` were standardized.
- Duplicate rows were removed.
- Missing values were not filled arbitrarily when reliable values were unavailable.

Missing values were handled carefully to avoid introducing unsupported assumptions that could affect the analysis.

## SQL Analysis

SQL was used to analyze employee salaries, employee counts, and performance across departments, cities, job roles, and experience levels.

## Charts & Data Visualization

The project includes five charts:

1. Average Salary by City
2. Average Salary by Experience
3. Employee Performance by Department
4. Employees by Department
5. Average Salary by Job Role

## Key Findings

- Ahmedabad had the highest average salary among the cities analyzed.
- Analyst was the job role with the highest average salary.
- The Marketing department had the highest number of employees.
- The analysis showed no major overall relationship between experience and average salary. However, average salary appeared to be higher for employees with more than 14 years of experience.
- The IT department had highest number of poor employees

## Conclusion

This project helped me practice data cleaning using Python and Pandas, analyze employee data using SQL, and create visualizations using Matplotlib. The analysis explored salary differences across cities, job roles, and experience levels, as well as employee performance across departments. This project improved my practical skills in data analysis and working with MySQL databases.