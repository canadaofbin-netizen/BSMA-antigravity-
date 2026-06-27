import subprocess

with open('temp_BSMA0001.json', 'r', encoding='utf-8') as f:
    data = f.read()

subprocess.run(['python', '.agents/scripts/universal_excel_inserter.py', '--excel', 'BSMA_Master_Coding_Sheet.xlsx', '--data', data], check=True)
