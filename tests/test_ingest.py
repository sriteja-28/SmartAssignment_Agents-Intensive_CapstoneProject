import os
from app.agents.ingest_agent import IngestAgent

def test_ingest():
    path = "tests/sample_pdfs/sample1.pdf"
    if not os.path.exists(path):
        print("place a sample PDF at tests/sample_pdfs/sample1.pdf")
        return
    agent = IngestAgent()
    doc = agent.process_pdf(path, "test-doc")
    assert 'pages' in doc
    assert len(doc['pages']) > 0
