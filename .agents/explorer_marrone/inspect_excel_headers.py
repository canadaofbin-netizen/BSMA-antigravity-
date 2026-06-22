import pandas as pd

excel_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\BSMA_Actual Coding Sheet_v5.xlsx"
df = pd.read_excel(excel_path, header=None)

# Let's print the first 4 rows for all columns
for r in range(4):
    print(f"\n--- Row {r} ---")
    row_vals = df.iloc[r].tolist()
    for c_idx, val in enumerate(row_vals):
        if pd.notna(val):
            print(f"Col {c_idx+1}: {val}")
