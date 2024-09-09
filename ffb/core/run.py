import os
import subprocess
from ffb.core.analyzer import ErrorAnalyzer


class Command:
    def __init__(self, raw):
        if ";" in raw:
            parts = raw.split(";")
            self.full_command = parts[1].strip()
        else:
            self.full_command = raw.strip()


class ShellHistory:
    def __init__(self, shell):
        self.shell = shell
        self.history_file = self._determine_history_file()

    def _determine_history_file(self):
        if self.shell == "zsh":
            return os.path.expanduser("~/.zsh_history")
        elif self.shell == "bash":
            return os.path.expanduser("~/.bash_history")
        else:
            raise ValueError("Unsupported shell or shell could not be determined.")

    def get_last_command(self):
        try:
            with open(self.history_file, "rb") as f:
                lines = f.readlines()
                if lines:
                    command = Command(lines[-2].decode()).full_command
                    return command
        except Exception as e:
            print(f"Error: {e}")
        return None


class Shell:
    @staticmethod
    def get_current_shell():
        shell = os.environ.get("SHELL")
        if shell:
            return shell.split("/")[-1]
        return None


def execute_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        return stdout, stderr
    except Exception as e:
        print(f"Failed to execute command: {e}")
        return None, None


def main():
    try:
        shell = Shell.get_current_shell()
        if not shell:
            raise ValueError("Shell could not be determined.")

        shell_history = ShellHistory(shell)
        last_command = shell_history.get_last_command()

        if last_command:
            stdout, stderr = execute_command(last_command)
            if stderr:
                analyzer = ErrorAnalyzer(stderr)
                analyzer.analyze_error()
        else:
            print("No command found in history.")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
