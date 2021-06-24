USE ABC_Company;

BULK INSERT Employee
FROM 'C:\\Users\\Collin\\Desktop\\Coding\\PumpJack Dataworks Coding Challenge\\emp_df.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2);