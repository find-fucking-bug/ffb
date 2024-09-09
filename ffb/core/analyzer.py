from ollama import Client
from ffb.utils.conf import settings


class ErrorAnalyzer:
    def __init__(self, output):
        """
        Initialize the ErrorAnalyzer with the given output.
        """
        self.output = output

    def generate_prompt(self):
        """
        Generate the AI prompt with the given output.
        """
        prompt = f"""
        Error Summary: Briefly explain the cause of the error.
        Solution: Provide a code example first, followed by a brief explanation of how it resolves the issue.

        Error:
        {self.output}
        """
        return prompt

    def analyze_error(self):
        """
        Send the AI prompt to the model and stream the response.
        """
        try:
            # Generate the prompt
            prompt = self.generate_prompt()

            # Send the chat request with the generated prompt and enable streaming
            client = Client(host=settings.OLLAMA_API_URL)
            stream = client.chat(
                model="llama3.1",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )

            # Loop through the streamed response chunks and print the content in real-time
            for chunk in stream:
                print(chunk["message"]["content"], end="", flush=True)

        except Exception as e:
            print(f"An error occurred: {e}")
