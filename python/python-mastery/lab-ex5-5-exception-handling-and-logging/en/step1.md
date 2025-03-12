# Understanding Exceptions in Python

In this step, we're going to learn about exceptions in Python. Exceptions are an important concept in programming. They help us deal with unexpected situations that can occur while a program is running. We'll also figure out why the current code crashes when it tries to process invalid data. Understanding this will help you write more robust and reliable Python programs.

## What are Exceptions?

In Python, exceptions are events that happen during the execution of a program and disrupt the normal flow of instructions. Think of it like a roadblock on a highway. When everything goes smoothly, your program follows a set path, just like a car on a clear road. But when an error occurs, Python creates an exception object. This object is like a report that contains information about what went wrong, such as the type of error and where it happened in the code.

If these exceptions are not properly handled, they cause the program to crash. When a crash occurs, Python shows a traceback message. This message is like a map that shows you the exact location in the code where the error occurred. It's very useful for debugging.

## Examining the Current Code

Let's first take a look at the `reader.py` file structure. This file contains functions that are used to read and convert CSV data. To open the file in the editor, we need to navigate to the correct directory. We'll use the `cd` command in the terminal.

```bash
cd /home/labex/project
```

Now that we're in the right directory, let's look at the content of `reader.py`. This file has several important functions:

1. `convert_csv()`: This function takes rows of data and uses a provided converter function to convert them. It's like a machine that takes raw materials (data rows) and turns them into a different form according to a specific recipe (the converter function).
2. `csv_as_dicts()`: This function reads CSV data and turns it into a list of dictionaries. It also performs type conversion, which means it makes sure that each piece of data in the dictionary is of the correct type, like a string, an integer, or a float.
3. `read_csv_as_dicts()`: This is a wrapper function. It's like a manager that calls the `csv_as_dicts()` function to get the job done.

## Demonstrating the Problem

Let's see what happens when the code tries to process invalid data. We'll open a Python interpreter, which is like a playground where we can test our Python code interactively. To open the Python interpreter, we'll use the following command in the terminal:

```bash
python3
```

Once the Python interpreter is open, we'll try to read the `missing.csv` file. This file contains some missing or invalid data. We'll use the `read_csv_as_dicts()` function from the `reader.py` file to read the data.

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
```

When you run this code, you should see an error message like this:

```
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: ''
```

This error occurs because the code tries to convert an empty string to an integer. An empty string doesn't represent a valid integer, so Python can't do the conversion. The function crashes at the first error it encounters, and it stops processing the rest of the valid data in the file.

To exit the Python interpreter, type the following command:

```python
exit()
```

## Understanding the Error Flow

The error happens in the `convert_csv()` function, specifically in the following line:

```python
return list(map(lambda row: converter(headers, row), rows))
```

The `map()` function applies the `converter` function to each row in the `rows` list. The `converter` function tries to apply the types (str, int, float) to each row. But when it encounters a row with missing data, it fails. The `map()` function doesn't have a built - in way to handle exceptions. So when an exception occurs, the entire process crashes.

In the next step, you'll modify the code to handle these exceptions gracefully. This means that instead of crashing, the program will be able to deal with the errors and continue processing the rest of the data.
