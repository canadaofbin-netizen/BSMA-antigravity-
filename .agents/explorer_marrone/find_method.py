with open("paper_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

# Find occurrences of "Method"
for idx, line in enumerate(lines):
    if "method" in line.lower() and len(line.strip()) < 30:
        # Check if it looks like a section header
        print(f"Line {idx}: {line}")
