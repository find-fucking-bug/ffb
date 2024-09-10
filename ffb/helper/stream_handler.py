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
        self.chunk_count = 1

    def process_stream(self):
        """
        Processes the incoming data chunks from the stream. As each chunk is received, it appends the content
        to `response_parts` and updates the progress bar. The total chunks in the progress bar are dynamically
        adjusted if more chunks are received than initially estimated.
        """
        # Initialize the progress bar and immediately set it to 5%
        initial_progress = 5
        with tqdm(
            total=self.total_chunks, desc="Loading response...", ncols=100
        ) as pbar:
            pbar.update(initial_progress)  # Quick update to 5%
            self.chunk_count += (
                initial_progress  # Reflect the initial progress in the chunk count
            )

            for chunk in self.stream:
                content = chunk["message"]["content"]
                self.response_parts.append(content)
                self.chunk_count += 1
                pbar.update(1)

                # Dynamically increase the total if necessary
                if self.chunk_count >= (pbar.total - 15):
                    pbar.total += 1
                    pbar.refresh()

            # Speed up the last 5% to finish quickly
            remaining = pbar.total - pbar.n
            pbar.update(remaining)

    def get_full_response(self):
        """
        Returns the full concatenated response after processing all the chunks.

        Returns:
            str: The complete response as a single string, formed by joining all the accumulated parts.
        """
        return "".join(self.response_parts)
