from app.tools.llm_wrapper import LLMWrapper

class QAAgent:
    def __init__(self, index_agent):
        self.index = index_agent
        self.llm = LLMWrapper()

    def answer(self, question, doc):
        hits = self.index.retrieve(question, top_k=5)
        context = '\n\n'.join([h['text'] for h in hits])
        prompt = self._build_prompt(question, context)
        ans = self.llm.generate(prompt)
        pages = list({h['meta']['page'] for h in hits})
        return {'answer': ans, 'pages': pages}

    def _build_prompt(self, question, context):
        return f"you are an assistant. use the context to answer concisely.\ncontext:\n{context}\nquestion: {question}\nanswer:"
