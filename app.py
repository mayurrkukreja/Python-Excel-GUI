from pandasgui import show

import pandas as pd

# Read Excel Sheet
file = 'details.xlsx'
# Get Data
data = pd.ExcelFile(file)

# Output Excel Sheet Names
print(data.sheet_names)
# Parse Data into Pandas Library
df = data.parse('details')

# Outputs all DataFields
print(df.head())

output = df[['CVE','Risk','Host','Synopsis','Description','Solution', 'Risk Factor']]
 
show(output)