import re

with open("paper_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for some patterns
print("=== Search for Age ===")
for m in re.finditer(r'(?i)\b(?:age|years\s+old|mean\s+age|average\s+age)\b', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    print(f"Context around index {m.start()}:")
    print(text[start:end].replace('\n', ' | '))
    print("-" * 50)

print("=== Search for Gender / Female / Men / Women ===")
for m in re.finditer(r'(?i)\b(?:female|women|gender|percent\s+female|percent\s+women|male|men)\b', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    print(f"Context around index {m.start()}:")
    print(text[start:end].replace('\n', ' | '))
    print("-" * 50)

print("=== Search for Tenure ===")
for m in re.finditer(r'(?i)\b(?:tenure|experience|work\s+experience|years\s+of\s+experience)\b', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    print(f"Context around index {m.start()}:")
    print(text[start:end].replace('\n', ' | '))
    print("-" * 50)
