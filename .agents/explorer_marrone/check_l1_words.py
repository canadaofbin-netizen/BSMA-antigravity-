import fitz

pdf_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\01_Academic_Papers\[18] Marrone Jennifer A., Tesluk Paul E., Carson Jay B. (2007) A Multilevel Investigation of Antecedents and Consequences of Team Member Boundary-Spanning Behavior.pdf"

doc = fitz.open(pdf_path)
page = doc[10] # page 11 is index 10

words = page.get_text("words")
# Word: (x0, y0, x1, y1, "text", block_no, line_no, word_no)
# Let's filter for words in the Level 1 table y-range (130 to 210)
table_words = [w for w in words if 130 <= w[1] <= 210]

# Sort by y first, then x
table_words.sort(key=lambda w: (w[1], w[0]))

print("Level 1 Table Words:")
for w in table_words:
    print(f"Word: '{w[4]}' at (x0={w[0]:.2f}, y0={w[1]:.2f}, x1={w[2]:.2f}, y1={w[3]:.2f})")
