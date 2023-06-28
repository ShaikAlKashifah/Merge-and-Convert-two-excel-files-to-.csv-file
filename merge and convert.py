#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read the two Excel files into pandas dataframes
df1 = pd.read_excel('titanic.xlsx')
df2 = pd.read_excel('salary.xlsx')

# Merge the two dataframes using the concat function
merged = pd.concat([df1, df2])

# Write the merged data to a new Excel file
merged.to_excel('merged.xlsx', index=False, encoding='utf-16')

read_file = pd.read_excel ('merged.xlsx')
read_file.to_csv ('new_merged.csv', index = None, header=True)


# In[ ]:




