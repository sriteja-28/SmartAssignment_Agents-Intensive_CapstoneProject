class SummaryAgent:
    def summarize(self, doc, max_sections=10):
        summaries = []
        for i, page in enumerate(doc['pages']):
            s = self._short_summary(page)
            summaries.append({'page': i+1, 'summary': s})
        return summaries

    def _short_summary(self, text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if not sentences:
            return ''
        return '. '.join(sentences[:2]) + ('.' if len(sentences) >= 2 else '')
