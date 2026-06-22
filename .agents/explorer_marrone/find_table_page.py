import fitz

pdf_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\01_Academic_Papers\[18] Marrone Jennifer A., Tesluk Paul E., Carson Jay B. (2007) A Multilevel Investigation of Antecedents and Consequences of Team Member Boundary-Spanning Behavior.pdf"

doc = fitz.open(pdf_path)
for page_num in range(len(doc)):
    text = doc[page_num].get_text("text")
    if "Descriptive Statistics and Correlations" in text:
        print(f"Table 1 is on page {page_num + 1}") # 1-indexed
