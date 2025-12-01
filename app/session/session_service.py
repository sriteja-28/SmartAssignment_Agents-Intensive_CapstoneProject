class SessionService:
    def __init__(self):
        self.sessions = {}

    def create_session(self, doc_id, doc):
        self.sessions[doc_id] = doc

    def get_session(self, doc_id):
        return self.sessions.get(doc_id)
