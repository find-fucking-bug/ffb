from tqdm import tqdm


class StreamResponseHandler:
    def __init__(self, stream, total_chunks=100):
        self.stream = stream
        self.response_parts = []
        self.total_chunks = total_chunks
        self.chunk_count = 0

    def process_stream(self):
        # Initialize the progress bar
        with tqdm(
            total=self.total_chunks, desc="Loading response...", ncols=100
        ) as pbar:
            for chunk in self.stream:
                content = chunk["message"]["content"]
                self.response_parts.append(content)
                self.chunk_count += 1

                # Update the progress bar
                pbar.update(1)

                # Dynamically adjust total chunks if needed
                if self.chunk_count >= pbar.total:
                    pbar.total += 50
                    pbar.refresh()

    def get_full_response(self):
        return "".join(self.response_parts)
