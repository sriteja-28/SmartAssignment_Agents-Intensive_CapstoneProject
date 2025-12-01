import os
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class LLMWrapper:
    def __init__(self):
        # get key from environment and remove trailing spaces/newlines
        self.api_key = os.environ.get("OPENAI_API_KEY", "").strip()
        if OPENAI_AVAILABLE and self.api_key:
            openai.api_key = self.api_key

    def generate(self, prompt, max_tokens=150):
        # use real API if available
        if OPENAI_AVAILABLE and self.api_key:
            try:
                resp = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens
                )
                return resp.choices[0].message['content'].strip()
            except openai.error.RateLimitError:
                # fallback if quota exceeded
                return "simulated answer (quota exceeded)"
            except Exception as e:
                # fallback on any other API error
                return f"simulated answer (API error: {str(e)})"
        # fallback if no key or OpenAI not installed
        return "simulated answer (no API key)"
