import openpyxl
import pandas as pd

excel_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\BSMA_Actual Coding Sheet_v5.xlsx"
df = pd.read_excel(excel_path)
print("Columns:")
for idx, col in enumerate(df.columns):
    print(f"Col {idx+1}: {col}")

print("\nShape:", df.shape)
print("\nUnique Article IDs:")
if 'Article ID' in df.columns:
    print(df['Article ID'].unique()[-5:])
elif 'Article ID (BSMAXXXX)' in df.columns:
    print(df['Article ID (BSMAXXXX)'].unique()[-5:])
else:
    # Try by position
    print(df.iloc[:, 1].unique()[-5:])
