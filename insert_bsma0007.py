import subprocess
import json
import os

data = {
    "article_id": "BSMA0007",
    "inclusion_status": 0,
    "exclusion_reason": "Boundary spanner is a department (team level)",
    "title": "A Comparative Organizational Study of Performance and Size Correlates in Inpatient Psychiatric Departments",
    "publication_name": "Administrative Science Quarterly",
    "author": "Hrebiniak et al.",
    "year": 1973
}

subprocess.run([
    "python", ".agents/scripts/universal_excel_inserter.py",
    "--excel", "BSMA_Master_Coding_Sheet.xlsx",
    "--data", json.dumps(data)
], check=True)
