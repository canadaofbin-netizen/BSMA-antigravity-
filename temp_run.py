import subprocess

json_data = '{"article_id": "BSMA0003", "inclusion_status": 0, "exclusion_reason": "File not found", "title": "", "publication_name": "", "author": "", "year": 999, "samples": []}'
subprocess.run(["python", ".agents/scripts/universal_excel_inserter.py", "--excel", "BSMA_Master_Coding_Sheet.xlsx", "--data", json_data])
