import sys

pdf_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\01_Academic_Papers\[18] Marrone Jennifer A., Tesluk Paul E., Carson Jay B. (2007) A Multilevel Investigation of Antecedents and Consequences of Team Member Boundary-Spanning Behavior.pdf"
txt_path = r"g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\.agents\explorer_marrone\paper_text.txt"

print("Python version:", sys.version)

libraries = ['pypdf', 'PyPDF2', 'pdfplumber', 'fitz', 'pdfminer']
available = []
for lib in libraries:
    try:
        __import__(lib)
        available.append(lib)
    except ImportError:
        pass
print("Available PDF libraries:", available)

# Let's try to extract text using the first available library
extracted = False

if 'fitz' in available:
    import fitz
    print("Using PyMuPDF (fitz)...")
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    extracted = True
elif 'pdfplumber' in available:
    import pdfplumber
    print("Using pdfplumber...")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    extracted = True
elif 'pypdf' in available:
    import pypdf
    print("Using pypdf...")
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    extracted = True
elif 'PyPDF2' in available:
    import PyPDF2
    print("Using PyPDF2...")
    reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    extracted = True

if extracted:
    print("Successfully extracted to text file. Character count:", len(text))
else:
    print("No library could extract text or all failed.")
