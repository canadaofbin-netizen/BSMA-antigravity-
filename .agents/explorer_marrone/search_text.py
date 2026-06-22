with open("paper_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

def search_keywords(keywords, context=5):
    results = []
    for idx, line in enumerate(lines):
        for kw in keywords:
            if kw.lower() in line.lower():
                start = max(0, idx - context)
                end = min(len(lines), idx + context + 1)
                context_lines = []
                for i in range(start, end):
                    prefix = "-> " if i == idx else "   "
                    context_lines.append(f"{i:4d}: {prefix}{lines[i]}")
                results.append((idx, kw, "\n".join(context_lines)))
                break # Only match first keyword in line
    return results

print("=== SEARCH FOR DEMOGRAPHICS (N, Age, Female, Tenure, Occupation, Country) ===")
dem_matches = search_keywords(["participants", "sample", "female", "women", "tenure", "age", "occupat", "country", "location"], 3)
# Let's print the first 30 matches to see
for idx, kw, match in dem_matches[:40]:
    print(f"Match for '{kw}' at line {idx}:")
    print(match)
    print("-" * 50)
