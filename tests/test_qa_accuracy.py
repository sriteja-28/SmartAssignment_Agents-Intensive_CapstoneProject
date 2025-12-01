from app.agents.qa_agent import QAAgent
from app.agents.index_agent import IndexAgent

def test_qa_simulation():
    index = IndexAgent()
    index.add_chunks([
        {'text': 'The sky is blue', 'meta': {'page':1}},
        {'text': 'Grass is green', 'meta': {'page':2}}
    ])
    qa = QAAgent(index)
    res = qa.answer("What color is the sky?", {'pages':[]})
    assert 'sky' in res['answer'].lower() or 'simulated' in res['answer'].lower()
