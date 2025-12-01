import os
from app.tools.pdf_parser import extract_text_by_page

class IngestAgent:
    def process_pdf(self, path, doc_id):
        title = os.path.basename(path)
        pages = extract_text_by_page(path)
        text = "\n\n".join(pages)
        return {
            'id': doc_id,
            'title': title,
            'page_count': len(pages),
            'pages': pages,
            'full_text': text,
        }
