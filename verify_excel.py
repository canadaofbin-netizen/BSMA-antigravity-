import pandas as pd

df = pd.read_excel('BSMA_Master_Coding_Sheet.xlsx')
print(df.tail(1).to_dict(orient='records'))
