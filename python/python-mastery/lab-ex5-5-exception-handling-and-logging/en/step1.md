# Understanding Exceptions in Python

In this step, you will learn about exceptions in Python and identify why the current code crashes when processing invalid data.

## What are Exceptions?

In Python, exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. When an error occurs, Python creates an exception object that contains information about the error.

If these exceptions are not properly handled, they cause the program to crash with a traceback message showing where the error occurred.

## Examining the Current Code

Let's first examine the `reader.py` file structure. Open the file in the editor:

```bash
cd /home/labex/project
```

Now, look at the content of `reader.py`. This file contains functions to read and convert CSV data:

1. `convert_csv()`: Converts rows of data using a provided converter function
2. `csv_as_dicts()`: Reads CSV data into a list of dictionaries with type conversion
3. `read_csv_as_dicts()`: A wrapper function that calls `csv_as_dicts()`

## Demonstrating the Problem

Let's see what happens when the code tries to process invalid data. Open a Python interpreter and try to read the `missing.csv` file that contains some missing or invalid data:

```bash
python3
```

In the Python interpreter, run:

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
```

You should see an error like this:

```
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: ''
```

The error occurs because the code tries to convert an empty string to an integer, which is not possible. The function crashes at the first error it encounters, without processing the rest of the valid data.

Exit the Python interpreter by typing:

```python
exit()
```

## Understanding the Error Flow

The error happens in the `convert_csv()` function, particularly in the line:

```python
return list(map(lambda row: converter(headers, row), rows))
```

When the converter function tries to apply the types (str, int, float) to a row with missing data, it fails. The `map()` function doesn't handle exceptions, causing the entire process to crash.

In the next step, you'll modify the code to handle these exceptions gracefully.
