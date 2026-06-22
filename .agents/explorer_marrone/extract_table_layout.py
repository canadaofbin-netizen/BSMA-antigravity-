import pdfplumber

pdf_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\01_Academic_Papers\[18] Marrone Jennifer A., Tesluk Paul E., Carson Jay B. (2007) A Multilevel Investigation of Antecedents and Consequences of Team Member Boundary-Spanning Behavior.pdf"

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[10] # page 11 is index 10
    
    # Try to extract tables
    tables = page.extract_tables()
    print(f"Extracted {len(tables)} tables with pdfplumber")
    for i, table in enumerate(tables):
        print(f"Table {i+1}:")
        for row in table:
            print(row)
        print("-" * 50)
        
    # Also print text with layout
    print("=== Text with layout ===")
    print(page.extract_text(layout=True))
