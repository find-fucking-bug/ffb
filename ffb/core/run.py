import os
import subprocess
from ffb.core.analyzer import ErrorAnalyzer


class Command:
    def __init__(self, raw):
        """
        Initialize the Command class by extracting the command part from the shell history line.
        """
        self.full_command = self._extract_command(raw)

    def _extract_command(self, raw):
        """
        Extracts and returns the full command from a raw shell history line.
        Handles cases where history may contain a timestamp or other metadata.
        """
        return raw.split(";")[-1].strip() if ";" in raw else raw.strip()


class ShellHistory:
    def __init__(self, shell):
        """
        Initialize the ShellHistory class with the shell type and history file location.
        """
        self.shell = shell
        self.history_file = self._determine_history_file()

    def _determine_history_file(self):
        """
        Determine the history file path based on the shell type.
        """
        history_files = {
            "zsh": "~/.zsh_history",
            "bash": "~/.bash_history",
        }
        return os.path.expanduser(history_files.get(self.shell, ""))

    def get_last_command(self):
        """
        Retrieve the last command from the shell history.
        Returns None if no command is found or an error occurs.
        """
        if not self.history_file:
            raise ValueError(
                f"Unsupported shell or shell history file could not be determined for {self.shell}."
            )

        try:
            with open(self.history_file, "rb") as f:
                lines = f.readlines()
                if lines:
                    return Command(lines[-2].decode()).full_command
        except Exception as e:
            print(f"Error reading history file: {e}")
        return None


class Shell:
    @staticmethod
    def get_current_shell():
        """
        Get the current shell by inspecting the environment variables.
        """
        shell_path = os.environ.get("SHELL")
        return shell_path.split("/")[-1] if shell_path else None


class CommandExecutor:
    @staticmethod
    def execute(command):
        """
        Execute the given shell command and return its stdout and stderr.
        """
        try:
            result = subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            print(f"Failed to execute command: {e}")
            return None, None


class ErrorHandler:
    def __init__(self, stderr_output):
        """
        Initialize the ErrorHandler with the command's stderr output.
        """
        self.stderr_output = stderr_output

    def analyze(self):
        """
        Analyze the error using the ErrorAnalyzer and display the result.
        """
        if self.stderr_output:
            analyzer = ErrorAnalyzer(self.stderr_output)
            analyzer.analyze_error()


def main():
    """
    Main function to get the last shell command, execute it, and handle any errors.
    """
    try:
        shell = Shell.get_current_shell()
        if not shell:
            raise ValueError("Shell could not be determined.")

        shell_history = ShellHistory(shell)
        last_command = shell_history.get_last_command()

        if last_command:
            stdout, stderr = CommandExecutor.execute(last_command)
            if stderr:
                ErrorHandler(stderr).analyze()
            else:
                print(f"Command executed successfully: {stdout}")
        else:
            print("No command found in history.")

    except ValueError as e:
        print(f"Error: {e}")
