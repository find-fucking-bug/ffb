# FFB: Find Fucking Bug
[![pypi](https://img.shields.io/pypi/v/ffb.svg?style=for-the-badge)](https://pypi.python.org/pypi/ffb)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
<a href="https://pypi.org/project/ffb" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/ffb.svg?style=for-the-badge" alt="Supported Python versions">
</a>
![Code Style - Ruff](https://img.shields.io/badge/code%20style-ruff-30173D.svg?style=for-the-badge)
![Pre Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)
[![ci](https://github.com/find-fucking-bug/ffb/workflows/CI/badge.svg?style=for-the-badge)](https://github.com/find-fucking-bug/ffb/actions?query=workflow:CI)

**FFB** is a Python package designed to simplify debugging by analyzing your terminal output and providing concise solutions and explanations for errors. Whether you're new to coding or an experienced developer, FFB aims to reduce the time spent deciphering cryptic error messages and helps you find solutions faster.

</hr>
<img align="left"  src="https://github.com/find-fucking-bug/ffb/blob/ffb-3/images/ffb.gif?raw=true">
</hr>


## Features

- Automatically analyzes the last terminal output.
- Provides clear explanations of errors.
- Suggests solutions with code examples.
- Easy-to-use command-line interface.

## Installation

You can install **FFB** via pip:

```bash
pip install ffb
```
## Usage

To use FFB, simply run your Python script as usual. If an error occurs, call ffb to analyze the last output.

## Example
Given the following Python code:

```python
def divide_numbers(a, b):
    result = a / b
    print(f"Result: {result}")

divide_numbers(10, 0)
```

Running this code will produce the following error:

```python
Traceback (most recent call last):
  File "/Users/aliymnx/Desktop/main.py", line 6, in <module>
    divide_numbers(10, 0)
  File "/Users/aliymnx/Desktop/main.py", line 2, in divide_numbers
    result = a / b
             ~~^~~
ZeroDivisionError: division by zero
```

To analyze this error using FFB, simply run:

```bash
ffb
```

FFB will analyze the error and provide a detailed solution:

```python
Error Summary The error occurs when attempting to divide a number by zero, which is undefined.

Solution

def divide_numbers(a, b):
   if b == 0:
      return "Error: Division by zero is not allowed."
  else:
    result = a / b
    return result

print(divide_numbers(10, 0))


Explanation To resolve this issue, we've added a simple check in the divide_numbers function to ensure that the divisor (b) is not zero. If it is zero, the function returns an error message instead of attempting the division, thus preventing the ZeroDivisionError.
```

## Self-hosting with Ollama

To run FFB in a self-hosted environment using Ollama, you’ll need to set the OLLAMA_API_URL environment variable. By default, you can set it to http://localhost:11434 if you’re running Ollama locally.

```bash
export OLLAMA_API_URL=http://localhost:11434
```
Ensure Ollama is running on your machine. You can find the setup and installation instructions for Ollama by visiting the [Ollama](https://ollama.com/) GitHub repository.

## Contributing

If you’d like to contribute to FFB, feel free to submit issues and pull requests on the GitHub repository.

## License
The license section now reflects the GPL-3.0 license as requested.
