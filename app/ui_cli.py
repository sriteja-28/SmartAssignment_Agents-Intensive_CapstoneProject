import os
from app.orchestrator import Orchestrator

DEMO_PDF = "tests/sample_pdfs/sample1.pdf"

def run_cli():
    print("smart assignment helper - demo")
    orch = Orchestrator()

    if not os.path.exists(DEMO_PDF):
        print("demo pdf missing: tests/sample_pdfs/sample1.pdf")
        return

    print("uploading demo pdf...")
    doc = orch.upload_pdf(DEMO_PDF)
    print(f"uploaded: {doc['title']} pages={doc['page_count']}")

    print("generating summaries...")
    summaries = orch.summarize_document(doc['id'])
    for i, s in enumerate(summaries[:3]):
        print(f"- section {i+1}: {s['summary'][:140]}")

    q = input('ask a question > ')
    ans = orch.answer_question(doc['id'], q)
    print("answer:")
    print(ans['answer'])
    print("source pages:", ans.get('pages'))

    if input('store a fact to memory? (y/n) ').strip().lower() == 'y':
        fact = input('enter fact > ')
        orch.store_memory(fact)
        print('fact saved')

    print('memory items:')
    mems = orch.list_memory()
    for m in mems:
        print('-', m)
