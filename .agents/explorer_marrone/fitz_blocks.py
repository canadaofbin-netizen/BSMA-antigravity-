import fitz

pdf_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\01_Academic_Papers\[18] Marrone Jennifer A., Tesluk Paul E., Carson Jay B. (2007) A Multilevel Investigation of Antecedents and Consequences of Team Member Boundary-Spanning Behavior.pdf"

doc = fitz.open(pdf_path)
page = doc[10] # page 11 is index 10

print("=== Blocks ===")
blocks = page.get_text("blocks")
for b in blocks:
    # b: (x0, y0, x1, y1, "text", block_no, block_type)
    print(f"Block {b[5]} (x0={b[0]:.1f}, y0={b[1]:.1f}, x1={b[2]:.1f}, y1={b[3]:.1f}):")
    print(b[4].replace('\n', ' | '))
    print("-" * 30)
