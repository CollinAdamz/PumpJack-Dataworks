USE ABC_Company;

BULK INSERT Department
FROM 'C:\\Users\\Collin\\Desktop\\Coding\\PumpJack Dataworks Coding Challenge\\dept_df.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2);