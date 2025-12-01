from app.session.memory_bank import MemoryBank

class MemoryAgent:
    def __init__(self):
        self.bank = MemoryBank()

    def save_fact(self, text):
        return self.bank.insert_fact(text)

    # rename or add alias so orchestrator works
    def list_memory(self):
        return [r['text'] for r in self.bank.list_all()]

    # keep the old method if needed
    def list_facts(self):
        return self.list_memory()
