import re

with open("paper_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for female or women or gender
print("=== Search for gender-related terms ===")
for m in re.finditer(r'(?i)\b(?:female|women|gender|male|men)\b', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    snippet = text[start:end].replace('\n', ' ')
    print(f"[{m.start()}]: {snippet}")
    print("-" * 50)

# Let's search for tenure or experience
print("\n=== Search for tenure/experience-related terms ===")
for m in re.finditer(r'(?i)\b(?:tenure|experience|months|years)\b', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    snippet = text[start:end].replace('\n', ' ')
    print(f"[{m.start()}]: {snippet}")
    print("-" * 50)
