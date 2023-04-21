import openai

class GPTAssistant:
    def __init__(self, api_key):
        # Initialize OpenAI API key and conversation history
        self.api_key = api_key
        openai.api_key = self.api_key
        self.conversation_history = []

    def generate_response(self, prompt):
        # Add user prompt to conversation history and generate response using GPT-3 model
        self.conversation_history.append({"role": "user", "content": prompt})
        messages = [{"role": "system", "content": "You are a helpful assistant."}] + self.conversation_history[-5:]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response_text = response.choices[0].message['content']
        self.conversation_history.append({"role": "assistant", "content": response_text})
        return response_text

def response_is_complete(response):
    # Check if the response ends with a period, question mark, or exclamation mark
    return response.strip().endswith(('.', '?', '!'))
