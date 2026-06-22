import pandas as pd

excel_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\BSMA_Actual Coding Sheet_v5.xlsx"
df = pd.read_excel(excel_path)

# Let's print the columns 0, 1, 2, 3, 4 for the last 15 rows
print("Last 15 rows:")
print(df.iloc[-15:, [0, 1, 2, 3, 4]])
