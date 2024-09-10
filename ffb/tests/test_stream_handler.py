import unittest
from unittest.mock import MagicMock
from ffb.helper.stream_handler import StreamResponseHandler


class TestStreamResponseHandler(unittest.TestCase):
    def setUp(self):
        """
        Set up mock stream and an instance of StreamResponseHandler.
        """
        # Mocking the stream with some sample chunks
        self.mock_stream = MagicMock()
        self.mock_stream.__iter__.return_value = [
            {"message": {"content": "chunk1"}},
            {"message": {"content": "chunk2"}},
            {"message": {"content": "chunk3"}},
        ]
        self.handler = StreamResponseHandler(self.mock_stream, total_chunks=3)

    def test_process_stream(self):
        """
        Test that the process_stream correctly processes the chunks and updates the progress bar.
        """
        # Run the stream processing
        self.handler.process_stream()

        # Check that all chunks have been processed and stored
        expected_response_parts = ["chunk1", "chunk2", "chunk3"]
        self.assertEqual(self.handler.response_parts, expected_response_parts)

        # Adjust expected chunk count based on the initial progress (5) + 3 chunks processed
        self.assertEqual(
            self.handler.chunk_count, 9
        )  # Initial progress starts at 5, then 3 chunks

    def test_get_full_response(self):
        """
        Test that get_full_response correctly concatenates the processed chunks.
        """
        # Process the stream first
        self.handler.process_stream()

        # Get the full response
        full_response = self.handler.get_full_response()

        # Check if the full response is concatenated correctly
        expected_full_response = "chunk1chunk2chunk3"
        self.assertEqual(full_response, expected_full_response)


if __name__ == "__main__":
    unittest.main()
