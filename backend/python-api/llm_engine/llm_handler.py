import openai
from anthropic import Client as AnthropicClient

class LLMHandler:
    def __init__(self, openai_api_key=None, anthropic_api_key=None):
        self.openai_api_key = openai_api_key
        self.anthropic_client = AnthropicClient(anthropic_api_key) if anthropic_api_key else None

    def generate_openai_prompt(self, prompt):
        openai.api_key = self.openai_api_key
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['choices'][0]['message']['content']

    def generate_anthropic_prompt(self, prompt):
        response = self.anthropic_client.completions.create(
            model='claude-1',
            prompt=prompt
        )
        return response['completion']

    def generate_ollama_prompt(self, model, prompt):
        import requests
        response = requests.post(f'http://localhost:11434/generate', json={'model': model, 'prompt': prompt})
        return response.json()['completion']

# Usage Example:
# llm_handler = LLMHandler(openai_api_key='your_openai_api_key',
#                       anthropic_api_key='your_anthropic_api_key')
# print(llm_handler.generate_openai_prompt('Tell me a joke!'))
# print(llm_handler.generate_anthropic_prompt('Tell me a joke!'))
# print(llm_handler.generate_ollama_prompt('llama-13b', 'Tell me a joke!'))