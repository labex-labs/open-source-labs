# Implementing Exception Handling

In this step, we'll focus on making your code more robust. When a program encounters bad data, it often crashes. But we can use a technique called exception handling to deal with these issues gracefully. You'll modify the `reader.py` file to implement this. Exception handling allows your program to continue running even when it faces unexpected data, instead of abruptly stopping.

## Understanding Try-Except Blocks

Python provides a powerful way to handle exceptions using try-except blocks. Let's break down how they work.

```python
try:
    # Code that might cause an exception
    result = risky_operation()
except SomeExceptionType as e:
    # Code that runs if the exception occurs
    handle_exception(e)
```

In the `try` block, you put the code that might raise an exception. An exception is an error that occurs during the execution of a program. For example, if you try to divide a number by zero, Python will raise a `ZeroDivisionError` exception. When an exception occurs in the `try` block, Python stops executing the code in the `try` block and jumps to the matching `except` block. The `except` block contains the code that will handle the exception. The `SomeExceptionType` is the type of exception you want to catch. You can catch specific types of exceptions or use a general `Exception` to catch all types of exceptions. The `as e` part allows you to access the exception object, which contains information about the error.

## Modifying the Code

Now, let's apply what we've learned about try-except blocks to the `convert_csv()` function. Open the `reader.py` file in your editor.

1. Replace the current `convert_csv()` function with the following code:

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

In this new implementation:

- We use a `for` loop instead of `map()` to process each row. This gives us more control over the processing of each row.
- We wrap the conversion code in a try-except block. This means that if an exception occurs during the conversion of a row, the program won't crash. Instead, it will jump to the `except` block.
- In the `except` block, we print an error message for invalid rows. This helps us identify which rows have issues.
- After printing the error message, we use the `continue` statement to skip the current row and continue processing the remaining rows.

Save the file after making these changes.

## Testing Your Changes

Let's test your modified code with the `missing.csv` file. First, open the Python interpreter by running the following command in your terminal:

```bash
python3
```

Once you're in the Python interpreter, run the following code:

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

When you run this code, you should see error messages for each problematic row. But the program will continue processing and return the valid rows. Here's an example of what you might see:

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

Let's also verify that the program works correctly with valid data. Run the following code in the Python interpreter:

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

You should see that all rows are processed without errors. Here's an example of the output:

```
Number of valid rows processed: 17
```

To exit the Python interpreter, run the following command:

```python
exit()
```

Now your code is more robust. It can handle invalid data gracefully by skipping bad rows instead of crashing. This makes your program more reliable and user-friendly.
