from PyPDF2 import PdfReader

def extract_text_by_page(path):
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        pages.append(text or "")
    return pages
