# FFB: Find Fucking Bug

**FFB** is a Python package designed to simplify debugging by analyzing your terminal output and providing concise solutions and explanations for errors. Whether you're new to coding or an experienced developer, FFB aims to reduce the time spent deciphering cryptic error messages and helps you find solutions faster.

<img align="left" width="100" height="100" src="https://picsum.photos/100/100">


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

```bash
╭───────────────────────────────────────────────────────────────────────────────────────────────────── Error Analysis Response ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Error Summary The error occurs when trying to divide a number by zero.                                                                                                                                                            │
│                                                                                                                                                                                                                                   │
│ Solution                                                                                                                                                                                                                          │
│                                                                                                                                                                                                                                   │
│  def divide_numbers(a, b):                                                                                                                                                                                                        │
│      if b == 0:                                                                                                                                                                                                                   │
│          print("Error: Division by zero is not allowed.")                                                                                                                                                                         │
│      else:                                                                                                                                                                                                                        │
│          result = a / b                                                                                                                                                                                                           │
│          print(f"The result of the division is {result}")                                                                                                                                                                         │
│                                                                                                                                                                                                                                   │
│  divide_numbers(10, 0)                                                                                                                                                                                                            │
│                                                                                                                                                                                                                                   │
│ In this code example, we added a simple check to see if b (the divisor) is equal to zero. If it is, we print an error message instead of attempting to perform the division. This prevents the ZeroDivisionError from occurring.  │
│                                                                                                                                                                                                                                   │
│ Explanation This solution resolves the issue by handling the special case where the divisor is zero. By adding a conditional statement to check for this scenario, we can avoid attempting to divide by zero and prevent the      │
│ error from occurring.                                                                                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────                                                                                                                                                                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

## Contributing

If you’d like to contribute to FFB, feel free to submit issues and pull requests on the GitHub repository.

## License
The license section now reflects the GPL-3.0 license as requested.
