# Implementing Exception Handling

In this step, you will modify the `reader.py` file to handle exceptions gracefully instead of crashing when it encounters bad data.

## Understanding Try-Except Blocks

Python uses try-except blocks to handle exceptions:

```python
try:
    # Code that might cause an exception
    result = risky_operation()
except SomeExceptionType as e:
    # Code that runs if the exception occurs
    handle_exception(e)
```

When an exception occurs in the `try` block, Python jumps to the matching `except` block instead of crashing.

## Modifying the Code

Let's modify the `convert_csv()` function to handle exceptions. Open the `reader.py` file in the editor:

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

This new implementation:

- Uses a for loop instead of `map()` to process each row
- Wraps the conversion in a try-except block
- Prints an error message for invalid rows
- Continues processing the remaining rows instead of crashing

Save the file after making these changes.

## Testing Your Changes

Let's test your modified code with the `missing.csv` file:

```bash
python3
```

In the Python interpreter, run:

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

You should see error messages for each problematic row, but the program continues processing and returns the valid rows:

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

Let's also verify the program works correctly with valid data:

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

You should see all rows processed without errors:

```
Number of valid rows processed: 17
```

Exit the Python interpreter:

```python
exit()
```

Now your code is more robust and can handle invalid data gracefully by skipping bad rows instead of crashing.
