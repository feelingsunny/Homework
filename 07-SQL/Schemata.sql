
--From ERD export
CREATE TABLE "dept_manager" (
  "dept_No" Varchar,
  "emp_No" Int,
  "from_date" Date,
  "to_date" Date,
  PRIMARY KEY ("dept_No", "emp_No")
);

CREATE TABLE "department" (
  "dept_No" Varchar,
  "dept_Name" Varchar,
  PRIMARY KEY ("dept_No")
);

CREATE TABLE "dept_emp" (
  "emp_No" Int,
  "dept_No" Varchar,
  "from_date" Date,
  "to_date" Date,
  PRIMARY KEY ("emp_No", "dept_No")
);

CREATE TABLE "titles" (
  "emp_No" Int,
  "title" Varchar,
  "from_date" Date,
  "to_date" Date,
  PRIMARY KEY ("emp_No")
);

CREATE TABLE "salaries" (
  "emp_No" Int,
  "salary" Type,
  "from_date" Date,
  "to_date" Date,
  PRIMARY KEY ("emp_No")
);

CREATE TABLE "employees" (
  "emp_No" Int,
  "birth_date" Date,
  "first_name" Varchar,
  "last_name" Varchar,
  "gender" Varchar,
  "hire_date" Date,
  PRIMARY KEY ("emp_No")
);







