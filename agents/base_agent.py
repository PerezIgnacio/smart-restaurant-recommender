import openai

class BaseAgent:
    def __init__(self, client, model="gpt-4o"):
        self.client = client
        self.model = model

    def llm(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.0,
            max_tokens=1024
        )

        return response.choices[0].message.content
