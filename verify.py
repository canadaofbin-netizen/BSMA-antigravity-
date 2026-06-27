import pandas as pd
df = pd.read_excel('BSMA_Master_Coding_Sheet.xlsx')
row = df[df['Article ID'] == 'BSMA0007'].iloc[0]
print(row[['Article ID', 'Inclusion-\nExclusion Judgment', 'Reason for Exclusion', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10']].to_dict())
