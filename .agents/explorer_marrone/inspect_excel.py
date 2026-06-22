import openpyxl
import pandas as pd

print("pandas version:", pd.__version__)
print("openpyxl version:", openpyxl.__version__)

df = pd.read_excel("BSMA_Actual Coding Sheet_v5.xlsx", sheet_name=0)
print("Columns:")
print(df.columns.tolist()[:30])
print("\nFirst 3 rows:")
print(df.iloc[:3, :15])
