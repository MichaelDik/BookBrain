import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        print(f"\n--- Page {page_num} ---\n{text}")

# Test with a small PDF (1-2 pages)
extract_text_from_pdf("PrideandPrejudice.pdf")
