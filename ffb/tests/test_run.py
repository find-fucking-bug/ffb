import unittest
from unittest.mock import patch, mock_open, MagicMock
from ffb.core.run import Command, ShellHistory, Shell, CommandExecutor, ErrorHandler


class TestCommand(unittest.TestCase):
    def test_extract_command_with_metadata(self):
        raw = "1629901345;ls -la"
        command = Command(raw)
        command._extract_command(raw)

    def test_extract_command_without_metadata(self):
        raw = "ls -la"
        command = Command(raw)
        command._extract_command(raw)


class TestShellHistory(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="1629901345;ls -la\n1629901345;pwd\n",
    )
    def test_get_last_command(self, mock_file):
        shell_history = ShellHistory(shell="bash")
        shell_history.get_last_command()

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_get_last_command_empty_history(self, mock_file):
        shell_history = ShellHistory(shell="bash")
        shell_history.get_last_command()


class TestShell(unittest.TestCase):
    @patch.dict("os.environ", {"SHELL": "/bin/bash"})
    def test_get_current_shell(self):
        Shell.get_current_shell()

    @patch.dict("os.environ", {"SHELL": ""})
    def test_get_current_shell_none(self):
        Shell.get_current_shell()


class TestCommandExecutor(unittest.TestCase):
    @patch("subprocess.run")
    def test_execute_success(self, mock_run):
        mock_result = MagicMock()
        mock_run.return_value = mock_result
        CommandExecutor.execute("ls")

    @patch("subprocess.run")
    def test_execute_failure(self, mock_run):
        mock_result = MagicMock()
        mock_run.return_value = mock_result
        CommandExecutor.execute("ls")


class TestErrorHandler(unittest.TestCase):
    @patch("ffb.core.analyzer.ErrorAnalyzer")
    def test_analyze(self, mock_analyzer):
        handler = ErrorHandler("Error")
        handler.analyze()


if __name__ == "__main__":
    unittest.main()
