import sys
import subprocess
import json

data = {
  "article_id": "BSMA0003",
  "inclusion_status": 1,
  "samples": [
    {
      "sample_number": 1,
      "sample_size": 192,
      "publication_type": 1,
      "study_design": 1,
      "international_context": 1,
      "occupation_type": "Junior doctors and APNs",
      "bs_measures": [
        {
          "name": "APN",
          "items": 999,
          "alpha": 999,
          "mean": 0.45,
          "sd": 0.50,
          "min": 999,
          "max": 999,
          "report_type": 1,
          "specific_measure": "An APN was present in 86 shifts.",
          "notes": "0 = No APN, 1 = APN"
        }
      ],
      "correlations": [
        {
          "non_bs_name": "Junior Doc. Experience",
          "r": -0.02,
          "alpha": 999,
          "mean": 2.06,
          "sd": 1.13,
          "items": 999,
          "min": 999,
          "max": 999,
          "report_type": 1,
          "specific_measure": "The average hospital experience of junior doctors.",
          "notes": "Years"
        },
        {
          "non_bs_name": "Paged requests for assistance",
          "r": -0.01,
          "alpha": 999,
          "mean": 11.46,
          "sd": 5.46,
          "items": 999,
          "min": 999,
          "max": 999,
          "report_type": 1,
          "specific_measure": "This information was taken from the pagers junior doctors carry on their overtime shift and recorded at the end of the shift.",
          "notes": "Count"
        },
        {
          "non_bs_name": "Tasks from day shift",
          "r": -0.16,
          "alpha": 999,
          "mean": 1.59,
          "sd": 1.92,
          "items": 999,
          "min": 999,
          "max": 999,
          "report_type": 1,
          "specific_measure": "Junior doctors recorded their tasks and self-initiated ward rounds throughout the overtime shift and also noted the origin of the task, such as whether the task could have been completed during the day.",
          "notes": "Count"
        },
        {
          "non_bs_name": "Skilled nurse/doctor tasks",
          "r": -0.26,
          "alpha": 999,
          "mean": 5.68,
          "sd": 4.70,
          "items": 999,
          "min": 999,
          "max": 999,
          "report_type": 1,
          "specific_measure": "Senior doctors and APNs also classified tasks into those that could be undertaken by junior doctors or skilled nurses (junior doctor/skilled nurse tasks) and tasks that could only be completed by junior doctors.",
          "notes": "Count"
        },
        {
          "non_bs_name": "Total tasks",
          "r": -0.16,
          "alpha": 999,
          "mean": 25.53,
          "sd": 13.03,
          "items": 999,
          "min": 999,
          "max": 999,
          "report_type": 1,
          "specific_measure": "Finally 'total tasks' was based on all tasks the junior doctor recorded during overtime.",
          "notes": "Count"
        },
        {
          "non_bs_name": "Self-initiated ward rounds",
          "r": 0.14,
          "alpha": 999,
          "mean": 1.61,
          "sd": 1.37,
          "items": 999,
          "min": 999,
          "max": 999,
          "report_type": 1,
          "specific_measure": "Junior doctors recorded their tasks and self-initiated ward rounds throughout the overtime shift...",
          "notes": "Count"
        }
      ]
    }
  ]
}

result = subprocess.run(
    ["python", ".agents/scripts/universal_excel_inserter.py", "--excel", "BSMA_Master_Coding_Sheet.xlsx", "--data", json.dumps(data)],
    capture_output=True,
    text=True
)

print(result.stdout)
if result.stderr:
    print("ERROR:", result.stderr)
