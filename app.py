import openpyxl
from pandasgui import show

import pandas as pd

# Read Excel Sheet
file = 'test.xlsx'
# Get Data
data = pd.ExcelFile(file)

# Outputs Excel Sheet Names
print(data.sheet_names)
# Parse Data into Pandas Library
df = data.parse('Sheet1')

# Outputs all DataFields
print(df.head())

output = df[['Name','RollNo','Address']]
show(output)


# Testing Code Below && Do not UnComment below code

# ps = openpyxl.load_workbook('test.xlsx')
# sheet = ps['Sheet1']

# print(ps['Name'].iloc[0])

# workbook = pd.read_excel('test.xlsx')

# # sheet = workbook['Sheet1']
# # print(workbook['Name'].iloc[0]) 
