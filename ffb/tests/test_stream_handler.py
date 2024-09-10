import unittest
from unittest.mock import MagicMock
from ffb.helper.stream_handler import StreamResponseHandler


class TestStreamResponseHandler(unittest.TestCase):
    def setUp(self):
        # Create a mock stream object
        self.mock_stream = MagicMock()
        # Fake data simulating the content of each chunk
        self.mock_stream.__iter__.return_value = [
            {"message": {"content": "Part 1"}},
            {"message": {"content": "Part 2"}},
            {"message": {"content": "Part 3"}},
        ]

        # Instantiate the StreamResponseHandler with the mock stream and total_chunks set to 3
        self.handler = StreamResponseHandler(self.mock_stream, total_chunks=3)

    def test_process_stream(self):
        # Call the method to process the stream
        self.handler.process_stream()

        # Ensure all chunks were processed and added to response_parts
        self.assertEqual(self.handler.response_parts, ["Part 1", "Part 2", "Part 3"])

    def test_get_full_response(self):
        # Process the stream to populate response_parts
        self.handler.process_stream()

        # Call get_full_response and check the full response string
        full_response = self.handler.get_full_response()
        self.assertEqual(full_response, "Part 1Part 2Part 3")


# Run the tests
if __name__ == "__main__":
    unittest.main()
