-- Create DB Object
CREATE DATABASE ABC_Company;

-- Use DB Object
USE ABC_Company;

-- Create Employee Table
CREATE TABLE Employee(
	id				varchar(36)  NOT NULL,
	first_name		Text		 NOT NULL,
	last_name		Text		 NOT NULL,
	salary			Numeric		 NOT NULL,
	department_id	varchar(36)	 NOT NULL
);

-- Create Department Table
CREATE TABLE Department(
	id					varchar(36)	NOT NULL,
	name				Text		NOT NULL,
	salary_increment	Numeric		NOT NULL
);

-- Add PK Constraint to Employee Table
ALTER TABLE Employee
ADD CONSTRAINT Emp_PK PRIMARY KEY(id)
;

-- Add Unique Constraint to Employee Table
ALTER TABLE Employee
ADD CONSTRAINT Unique_Emp_PK UNIQUE(id)
;

-- Add PK Constraint to Department Table
ALTER TABLE Department
ADD CONSTRAINT Dep_PK PRIMARY KEY(id)
;

-- Add Unique Constraint to Department Table
ALTER TABLE Department
ADD CONSTRAINT Unique_Dep_PK UNIQUE(id)
;

-- Add FK Constraint to Employee Table
ALTER TABLE Employee
ADD CONSTRAINT Emp_FK 
FOREIGN KEY(department_id) REFERENCES Department(id)
;
