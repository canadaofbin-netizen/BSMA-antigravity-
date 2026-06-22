import pandas as pd

excel_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\BSMA_Actual Coding Sheet_v5.xlsx"
df = pd.read_excel(excel_path)

# Print last 10 rows
print("Last 10 rows:")
print(df.iloc[-10:, :6])
