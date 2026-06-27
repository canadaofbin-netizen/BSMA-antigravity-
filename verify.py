import pandas as pd

df = pd.read_excel('BSMA_Master_Coding_Sheet.xlsx')
print(df[df['article_id'] == 'BSMA0008'].to_string())
