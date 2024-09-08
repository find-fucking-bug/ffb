import ollama


class ErrorAnalyzer:
    def __init__(self, traceback):
        """
        Initialize the ErrorAnalyzer with the given traceback.
        """
        self.traceback = traceback

    def generate_prompt(self):
        """
        Generate the AI prompt with the given traceback.
        """
        prompt = f"""
        Analyze the following error message, provide a brief summary of what caused the issue,
        and offer a clear solution to resolve it:

        {self.traceback}

        1. Error Summary: Provide a concise explanation of the error, describing its cause and the component it affects.
        2. Solution: Outline the steps or code changes required to fix the issue.
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
            stream = ollama.chat(
                model="llama3.1",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )

            # Loop through the streamed response chunks and print the content in real-time
            for chunk in stream:
                print(chunk["message"]["content"], end="", flush=True)

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    traceback_message = """
    Traceback (most recent call last):
      File "/Users/aliymnx/Desktop/ffb/ffb/core/deneme.py", line 5, in <module>
        main()
      File "/Users/aliymnx/Desktop/ffb/ffb/core/deneme.py", line 2, in main
        print(5+U)
                ^
    NameError: name 'U' is not defined
    """

    # Create an instance of the ErrorAnalyzer class and pass the traceback message
    analyzer = ErrorAnalyzer(traceback_message)

    # Analyze the error
    analyzer.analyze_error()
