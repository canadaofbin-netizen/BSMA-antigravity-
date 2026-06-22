with open("paper_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

print("=== Table References in Paper ===")
for m in re.finditer(r'(?i)\bTable\s+\d+\b', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    print(f"[{m.start()}]: {text[start:end].strip().replace('\n', ' ')}")
