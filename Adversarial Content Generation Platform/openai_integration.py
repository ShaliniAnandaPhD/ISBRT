##pip install requests
import requests

class OpenAIIntegration:
    def __init__(self, api_key):
        self.api_url = "https://api.openai.com/v1/engines/davinci/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }

    def send_prompt(self, prompt):
        try:
            data = {
                "prompt": prompt,
                "max_tokens": 150  # Adjust the number of tokens as needed
            }
            response = requests.post(self.api_url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["text"]
        except requests.RequestException as e:
            print(f"Error communicating with OpenAI API: {e}")
            return None
