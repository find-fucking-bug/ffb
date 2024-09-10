from rich.progress import Progress, BarColumn, TextColumn
from rich.console import Console


class StreamResponseHandler:
    """
    Handles the processing of a streamed response, displaying a progress bar as it accumulates the data
    and returns the full response when completed.
    """

    def __init__(self, stream, total_chunks=100):
        """
        Initializes the StreamResponseHandler with the stream object and an optional number of total chunks.

        Args:
            stream: The stream object from which the response is retrieved.
            total_chunks (int, optional): Initial estimate of the number of chunks expected in the stream.
            Defaults to 100.
        """
        self.stream = stream
        self.response_parts = []
        self.total_chunks = total_chunks
        self.chunk_count = 1

    def process_stream(self):
        """
        Processes the incoming data chunks from the stream. As each chunk is received, it appends the content
        to `response_parts` and updates the progress bar. The total chunks in the progress bar are dynamically
        adjusted if more chunks are received than initially estimated.
        """
        # Initialize the progress bar and set initial progress
        console = Console()

        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
        ) as progress:
            task = progress.add_task("Fetching results ...", total=self.total_chunks)

            # Start with initial progress at 5%
            initial_progress = 5
            progress.update(task, advance=initial_progress)
            self.chunk_count += initial_progress

            # Iterate over the chunks from the stream
            for chunk in self.stream:
                content = chunk["message"]["content"]
                self.response_parts.append(content)
                self.chunk_count += 1

                # Update the progress bar
                progress.update(task, advance=1)

                # Dynamically increase the total if necessary
                if self.chunk_count >= (progress.tasks[task].total - 15):
                    progress.update(task, total=progress.tasks[task].total + 1)

            # Speed up the last 5% to finish quickly
            remaining = progress.tasks[task].total - progress.tasks[task].completed
            progress.update(task, advance=remaining)

    def get_full_response(self):
        """
        Returns the full concatenated response after processing all the chunks.

        Returns:
            str: The complete response as a single string, formed by joining all the accumulated parts.
        """
        return "".join(self.response_parts)
