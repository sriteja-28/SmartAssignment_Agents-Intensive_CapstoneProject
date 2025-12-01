import uuid
from app.agents.ingest_agent import IngestAgent
from app.agents.index_agent import IndexAgent
from app.agents.summary_agent import SummaryAgent
from app.agents.qa_agent import QAAgent
from app.agents.memory_agent import MemoryAgent
from app.session.session_service import SessionService

class Orchestrator:
    def __init__(self):
        self.ingest = IngestAgent()
        self.index = IndexAgent()
        self.summary = SummaryAgent()
        self.qa = QAAgent(self.index)
        self.memory = MemoryAgent()
        self.sessions = SessionService()

    def upload_pdf(self, path):
        doc_id = str(uuid.uuid4())
        doc = self.ingest.process_pdf(path, doc_id)
        self.index.index_document(doc)
        self.sessions.create_session(doc_id, doc)
        return doc

    def summarize_document(self, doc_id):
        doc = self.sessions.get_session(doc_id)
        return self.summary.summarize(doc)

    def answer_question(self, doc_id, question):
        doc = self.sessions.get_session(doc_id)
        return self.qa.answer(question, doc)

    def store_memory(self, text):
        return self.memory.save_fact(text)

    def list_memory(self):
        return self.memory.list_memory()
