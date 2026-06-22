import pandas as pd

excel_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\BSMA_Actual Coding Sheet_v5.xlsx"
df = pd.read_excel(excel_path)

# Filter rows where Article ID is BSMA0008
marrone_coded = df[df['Article ID'] == 'BSMA0008']
print(f"Number of rows coded for BSMA0008: {len(marrone_coded)}")

# Let's print some columns for these rows
cols_to_print = ['Article ID', 'Sample ID', 'Effect size ID', 'Unnamed: 7', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 13']
# Let's check which columns are actually available
print("Coded row details:")
print(marrone_coded.iloc[:, [1, 2, 3, 4, 16, 21, 22, 23, 24, 25, 40, 44, 48]])
# Let's print the actual values of column 41 (Boundary spanning variable name) and column 45 (other variable name) and column 49 (r)
print("\nVariable names and r:")
print(marrone_coded.iloc[:, [1, 2, 3, 40, 44, 48]])
