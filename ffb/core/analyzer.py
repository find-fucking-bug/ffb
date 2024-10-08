from ollama import Client
from ffb.helper.stream_handler import StreamResponseHandler
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import os


class ErrorAnalyzer:
    def __init__(self, output):
        """
        Initialize the ErrorAnalyzer with the given output.
        """
        self.output = output
        self.console = Console()
        self.ollama_api_url = os.getenv("OLLAMA_API_URL", "http://localhost:11434")

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
        Send the AI prompt to the model and stream the response, then print the output using rich.
        """
        try:
            # Generate the prompt
            prompt = self.generate_prompt()

            # Send the chat request with the generated prompt and enable streaming
            client = Client(host=self.ollama_api_url)
            stream = client.chat(
                model="llama3.1",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            handler = StreamResponseHandler(stream)
            handler.process_stream()
            response = handler.get_full_response()

            # Convert the response to Markdown for rich rendering
            markdown_response = Markdown(response)

            # Display the response using rich in markdown format
            self.console.print(
                Panel.fit(
                    markdown_response,
                    title="Error Analysis",
                    border_style="green",
                    padding=(1, 2),
                    safe_box=True,
                )
            )

        except Exception as e:
            self.console.print(f"[bold red]An error occurred:[/bold red] {e}")
