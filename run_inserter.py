import sys
import subprocess
import json

data = {
  "article_id": "BSMA0002",
  "inclusion_status": 0,
  "exclusion_reason": "The paper is a qualitative study utilizing thematic analysis, not a quantitative empirical study, and does not contain a correlation matrix or measurable variables."
}

result = subprocess.run(
    ["python", ".agents/scripts/universal_excel_inserter.py", "--excel", "BSMA_Master_Coding_Sheet.xlsx", "--data", json.dumps(data)],
    capture_output=True,
    text=True
)

print(result.stdout)
if result.stderr:
    print("ERROR:", result.stderr)
