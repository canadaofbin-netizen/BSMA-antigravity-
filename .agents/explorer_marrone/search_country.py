with open("paper_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
print("=== Search for Country/State ===")
for m in re.finditer(r'(?i)\b(?:united states|u\.s\.|usa|american|mid-atlantic|atlantic)\b', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    print(text[start:end].replace('\n', ' '))
    print("-" * 50)
