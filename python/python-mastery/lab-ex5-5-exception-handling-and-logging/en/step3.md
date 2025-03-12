# Implementing Logging

In this step, you will enhance your code by replacing the simple print messages with proper logging using Python's `logging` module.

## Understanding the Logging Module

The `logging` module in Python provides a flexible framework for emitting log messages from applications. It offers more features than simple print statements:

1. Different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
2. Configurable output format
3. Messages can be directed to different outputs (console, files, etc.)
4. Log filtering based on severity

## Adding Logging to reader.py

Let's modify your code to use the logging module. Open the `reader.py` file:

1. First, add the import statement at the top of the file:

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

2. Now modify the `convert_csv()` function to use logging instead of print statements:

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
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

The key changes here:

- Replace `print()` with `logger.warning()` for the error message
- Add a new `logger.debug()` message with details about the exception
- The `str(e)` converts the exception to a string, displaying the error reason

Save the file after making these changes.

## Testing Logging

Let's test your code with logging enabled:

```bash
python3
```

In the Python interpreter, execute:

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

You should see output like this:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

Notice that the logging module prefixes each message with the level (WARNING/DEBUG) and module name.

Let's see what happens if we change the log level to only show warnings:

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Now you'll only see the WARNING messages, but not the DEBUG messages:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

This demonstrates the benefit of using different logging levels - you can control how much detail is shown without changing your code.

Exit the Python interpreter:

```python
exit()
```

Congratulations! You've now implemented proper exception handling and logging in your Python program. This approach makes your code more robust and provides better diagnostic information when errors occur.
