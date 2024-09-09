from tqdm import tqdm


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
        self.chunk_count = 0

    def process_stream(self):
        """
        Processes the incoming data chunks from the stream. As each chunk is received, it appends the content
        to `response_parts` and updates the progress bar. The total chunks in the progress bar are dynamically
        adjusted if more chunks are received than initially estimated.
        """
        # Initialize the progress bar
        with tqdm(
            total=self.total_chunks, desc="Loading response...", ncols=100
        ) as pbar:
            for chunk in self.stream:
                content = chunk["message"]["content"]
                self.response_parts.append(
                    content
                )  # Append each chunk's content to the response list
                self.chunk_count += 1

                # Update the progress bar as each chunk is received
                pbar.update(1)

                # Dynamically adjust total chunks if needed
                if self.chunk_count >= pbar.total:
                    pbar.total += (
                        25  # Extend the progress bar if more chunks are expected
                    )
                    pbar.refresh()

    def get_full_response(self):
        """
        Returns the full concatenated response after processing all the chunks.

        Returns:
            str: The complete response as a single string, formed by joining all the accumulated parts.
        """
        return "".join(self.response_parts)
