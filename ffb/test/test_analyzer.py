import unittest
from unittest.mock import patch, MagicMock
from rich.console import Console
from ffb.core.analyzer import ErrorAnalyzer


class TestErrorAnalyzer(unittest.TestCase):
    def setUp(self):
        self.error_output = "SyntaxError: invalid syntax"
        self.analyzer = ErrorAnalyzer(self.error_output)

    def test_generate_prompt(self):
        prompt = self.analyzer.generate_prompt()
        expected_prompt = f"""
        Error Summary: Briefly explain the cause of the error.
        Solution: Provide a code example first, followed by a brief explanation of how it resolves the issue.

        Error:
        {self.error_output}
        """
        self.assertEqual(prompt.strip(), expected_prompt.strip())

    @patch("ffb.core.analyzer.StreamResponseHandler")
    @patch("ollama.Client.chat")
    def test_analyze_error(self, mock_chat, mock_stream_handler):
        mock_stream_handler_instance = MagicMock()
        mock_stream_handler.return_value = mock_stream_handler_instance
        mock_stream_handler_instance.get_full_response.return_value = "Test response"
        mock_chat.return_value = [{"message": {"content": "Test message"}}]
        with patch.object(Console, "print") as mock_console_print:
            self.analyzer.analyze_error()
            mock_stream_handler.assert_called_once()
            mock_console_print.assert_called()


if __name__ == "__main__":
    unittest.main()
