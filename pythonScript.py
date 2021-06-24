#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries
import pyodbc
import pandas as pd
import numpy as np
import uuid
import os


# # Pre-process data file

# In[ ]:


# load csv file
path = 'C:\\Users\\Collin\\Desktop\\Coding\\PumpJack Dataworks Coding Challenge\\flat_data.csv'
wdir = 'C:\\Users\\Collin\\Desktop\\Coding\\PumpJack Dataworks Coding Challenge'
df = pd.read_csv(path)


# In[ ]:


# set working directory
os.chdir(wdir)

# check directory
os.getcwd()


# ### Department table pre-processing

# In[ ]:


# select relevent columns from file
dept_subset = df.iloc[:,[3,4]]

# save unique values to variables
unique_dept_nm_values = dept_subset.iloc[:,0].unique()
unique_inc_values = dept_subset.iloc[:,1].unique()

# create & fill list for UUIDs
dept_UUIDs = []
for val in range(0,len(unique_dept_nm_values)):
    dept_UUIDs.append(uuid.uuid1()) 
    
# convert list to np array
dept_UUIDs_np = np.array(dept_UUIDs)

# create df object
dept_df = pd.DataFrame()

# insert data into df object
dept_df["id"] = dept_UUIDs_np
dept_df["dept_name"] = unique_dept_nm_values.tolist()
dept_df["salary_increment"] = unique_inc_values.tolist()

# write new df to csv file
dept_df.to_csv("dept_df.csv", index = False)


# ### Employee table pre-processing

# In[ ]:


# select relevent columns from file
emp_subset = df.iloc[:,0:4]

# create & fill list for UUIDs
emp_UUIDs = []
for val in range(0,len(df.iloc[:,1])):
    emp_UUIDs.append(uuid.uuid1()) 
    
# convert list to np array
emp_UUIDs_np = np.array(emp_UUIDs)

# create df object
emp_df = pd.DataFrame()

# create dept_name dictionary - name:UUID
dept_id = dept_df[["id","dept_name"]]
dept_dict = dict([(i,a) for i,a in zip(dept_id['dept_name'],dept_id['id'])])
print(dept_dict)
# insert data into df object
emp_df["id"] = emp_UUIDs_np
emp_df["first_name"] = df[["first_name"]]
emp_df["last_name"] = df[["last_name"]]
emp_df["salary"] = df[["salary"]]
emp_df["department_id"] = df[["dept_name"]]
emp_df.replace({"department_id":dept_dict}, inplace=True)

# write new df to csv file
emp_df.to_csv("emp_df.csv", index = False)

