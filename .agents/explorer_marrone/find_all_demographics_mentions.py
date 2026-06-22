with open("paper_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

keywords = ["gender", "diversity", "demographic", "ethnic", "asian", "years", "months", "percent", "%", "female", "male", "tenure", "age", "experience"]

print("=== Search Results ===")
for idx, line in enumerate(lines):
    matched = []
    for kw in keywords:
        if kw in line.lower():
            matched.append(kw)
    if matched:
        print(f"Line {idx:4d} (matches: {matched}): {line.strip()}")
