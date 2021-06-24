USE ABC_Company;

SELECT 
	E.id AS Employee_id,
	((((
		SUM(D.salary_increment) / COUNT(D.salary_increment)
		) / 100
		) + 1
		) * 
		(SUM(E.salary)/COUNT(E.salary))
		) 
		AS Updated_salary
FROM 
	Employee AS E 
	JOIN Department AS D 
	ON E.department_id = D.id
GROUP BY E.id
;
