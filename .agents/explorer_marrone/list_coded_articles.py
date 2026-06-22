import pandas as pd

excel_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\BSMA_Actual Coding Sheet_v5.xlsx"
df = pd.read_excel(excel_path)

# Print unique articles (Article ID, Authors, Title)
unique_articles = df[['Article ID', 'Unnamed: 9', 'Unnamed: 7']].drop_duplicates().dropna(subset=['Article ID'])
for idx, row in unique_articles.iterrows():
    print(f"ID: {row['Article ID']}")
    print(f"  Authors: {row['Unnamed: 9']}")
    print(f"  Title: {row['Unnamed: 7']}")
    print("-" * 50)
