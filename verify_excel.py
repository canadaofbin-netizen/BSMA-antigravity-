import pandas as pd

try:
    df = pd.read_excel("BSMA_Master_Coding_Sheet.xlsx")
    print(df.tail(1).to_string())
except Exception as e:
    print("Error:", e)
