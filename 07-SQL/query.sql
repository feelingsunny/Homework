--Specify data types, primary keys, foreign keys, and other constraints.
DROP TABLE IF EXISTS departments;
CREATE TABLE departments(
	dept_No VARCHAR NOT NULL PRIMARY KEY,
	dept_Name VARCHAR NOT NULL);

SELECT * FROM departments;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees(
	emp_No INT NOT NULL PRIMARY KEY,
	birth_date DATE NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	gender VARCHAR(100) NOT NULL,
	hire_date date NOT NULL);

SELECT * FROM employees;

DROP TABLE IF EXISTS dept_emp;
CREATE TABLE dept_emp(
	emp_No INT NOT NULL,
	dept_No VARCHAR NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL,
	Primary Key (emp_No,dept_No),
	FOREIGN KEY (emp_No)  REFERENCES employees (emp_No)    ON DELETE CASCADE,
   	FOREIGN KEY (dept_No) REFERENCES departments (dept_No) ON DELETE CASCADE);

SELECT * FROM dept_emp;

DROP TABLE IF EXISTS dept_manager;
CREATE TABLE dept_manager(
	dept_No VARCHAR(10) NOT NULL,
	emp_No INT NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL,
	Primary Key (emp_No,dept_No),
	FOREIGN KEY (emp_No)  REFERENCES employees (emp_No)    ON DELETE CASCADE,
   	FOREIGN KEY (dept_No) REFERENCES departments (dept_No) ON DELETE CASCADE);

SELECT * FROM dept_manager;

DROP TABLE IF EXISTS salaries;
CREATE TABLE salaries(
	emp_No INT NOT NULL PRIMARY KEY,
	salary VARCHAR(100) NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL);

SELECT * FROM salaries;

DROP TABLE IF EXISTS titles;
CREATE TABLE titles(
	emp_No INT NOT NULL,
	title VARCHAR(100) NOT NULL,
	from_date DATE,
	to_date DATE,
	Primary Key (emp_No,title,from_date),
	FOREIGN KEY (emp_No)  REFERENCES employees (emp_No)  ON DELETE CASCADE);

SELECT * FROM titles;

--Import from ERD
SELECT 'postgresql' AS dbms,t.table_catalog,t.table_schema,t.table_name,c.column_name,c.ordinal_position,c.data_type,c.character_maximum_length,n.constraint_type,k2.table_schema,k2.table_name,k2.column_name FROM information_schema.tables t NATURAL LEFT JOIN information_schema.columns c LEFT JOIN(information_schema.key_column_usage k NATURAL JOIN information_schema.table_constraints n NATURAL LEFT JOIN information_schema.referential_constraints r)ON c.table_catalog=k.table_catalog AND c.table_schema=k.table_schema AND c.table_name=k.table_name AND c.column_name=k.column_name LEFT JOIN information_schema.key_column_usage k2 ON k.position_in_unique_constraint=k2.ordinal_position AND r.unique_constraint_catalog=k2.constraint_catalog AND r.unique_constraint_schema=k2.constraint_schema AND r.unique_constraint_name=k2.constraint_name WHERE t.TABLE_TYPE='BASE TABLE' AND t.table_schema NOT IN('information_schema','pg_catalog');


--1.List the following details of each employee: employee number, last name, first name,gender, and salary.
SELECT employees.emp_No, employees.last_name, employees.first_name, employees.gender, salaries.salary
FROM salaries
INNER JOIN employees ON
employees.emp_No=salaries.emp_No;

--2.List employees who were hired in 1986.
SELECT * 
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1987-01-01';

--3.List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT departments.dept_No, departments.dept_Name, dept_manager.emp_No, employees.last_name, employees.first_name, dept_manager.from_date, dept_manager.to_date
FROM departments 
INNER JOIN dept_manager ON
departments.dept_No = dept_manager.dept_No
INNER JOIN employees ON
dept_manager.emp_No = employees.emp_No;

--4.List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT departments.dept_No, departments.dept_Name, dept_manager.emp_No, employees.last_name, employees.first_name, dept_manager.from_date, dept_manager.to_date
FROM departments 
INNER JOIN dept_manager ON
departments.dept_No = dept_manager.dept_No
INNER JOIN employees ON
dept_manager.emp_No = employees.emp_No;

--5.List all employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name, last_name
FROM employees
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%'

--6.List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT departments.dept_Name, dept_emp.emp_No, employees.last_name, employees.first_name
FROM dept_emp 
INNER JOIN employees ON
dept_emp.emp_No = employees.emp_No
INNER JOIN departments ON
departments.dept_No = dept_emp.dept_No
WHERE departments.dept_name = 'Sales';

--7.List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT departments.dept_Name, dept_emp.emp_No, employees.last_name, employees.first_name
FROM dept_emp 
INNER JOIN employees ON
dept_emp.emp_No = employees.emp_No
INNER JOIN departments ON
departments.dept_No = dept_emp.dept_No
WHERE departments.dept_name = 'Sales'
OR departments.dept_name = 'Development';

--8.In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name,
COUNT(last_name) AS "frequency"
FROM employees
GROUP BY last_name
ORDER BY
COUNT(last_name) DESC;





