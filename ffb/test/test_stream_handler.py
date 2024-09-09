import unittest
from ffb.helper.stream_handler import StreamResponseHandler


class TestStreamResponseHandler(unittest.TestCase):
    def setUp(self):
        self.mock_stream = [
            {"message": {"content": "Chunk 1"}},
            {"message": {"content": "Chunk 2"}},
            {"message": {"content": "Chunk 3"}},
        ]
        self.handler = StreamResponseHandler(self.mock_stream, total_chunks=3)

    def test_process_stream(self):
        self.handler.process_stream()
        self.assertEqual(self.handler.chunk_count, 3)
        self.assertEqual(self.handler.response_parts, ["Chunk 1", "Chunk 2", "Chunk 3"])

    def test_get_full_response(self):
        self.handler.process_stream()
        full_response = self.handler.get_full_response()
        self.assertEqual(full_response, "Chunk 1Chunk 2Chunk 3")


if __name__ == "__main__":
    unittest.main()
