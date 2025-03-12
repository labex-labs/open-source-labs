# Implementing Logging

In this step, we're going to make your code better. Instead of using simple print messages, we'll use Python's `logging` module for proper logging. Logging is a great way to keep track of what your program is doing, especially when it comes to handling errors and understanding the flow of your code.

## Understanding the Logging Module

The `logging` module in Python gives us a flexible way to send out log messages from our applications. It's much more powerful than just using simple print statements. Here's what it can do:

1. Different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL): These levels help us categorize the importance of the messages. For example, DEBUG is for detailed information that's useful during development, while CRITICAL is for serious errors that might stop the program.
2. Configurable output format: We can decide how the log messages will look, like adding timestamps or other useful information.
3. Messages can be directed to different outputs (console, files, etc.): We can choose to show the log messages on the console, save them to a file, or even send them to a remote server.
4. Log filtering based on severity: We can control which messages we see based on their log level.

## Adding Logging to reader.py

Now, let's change your code to use the logging module. Open the `reader.py` file.

First, we need to import the `logging` module and set up a logger for this module. Add the following code at the top of the file:

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

The `import logging` statement brings in the `logging` module so we can use its functions. The `logging.getLogger(__name__)` creates a logger for this specific module. Using `__name__` ensures that the logger has a unique name related to the module.

Next, we'll modify the `convert_csv()` function to use logging instead of print statements. Here's the updated code:

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

The main changes here are:

- We replaced `print()` with `logger.warning()` for the error message. This way, the message is logged with the appropriate warning level, and we can control its visibility later.
- We added a new `logger.debug()` message with details about the exception. This gives us more information about what went wrong, but it's only shown if the logging level is set to DEBUG or lower.
- The `str(e)` converts the exception to a string, so we can display the error reason in the log message.

After making these changes, save the file.

## Testing Logging

Let's test your code with logging enabled. Open the Python interpreter by running the following command in your terminal:

```bash
python3
```

Once you're in the Python interpreter, execute the following code:

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Here, we first import the `logging` module and our `reader` module. Then, we set the logging level to DEBUG using `logging.basicConfig(level=logging.DEBUG)`. This means we'll see all log messages, including DEBUG, INFO, WARNING, ERROR, and CRITICAL. We then call the `read_csv_as_dicts` function from the `reader` module and print the number of valid rows processed.

You should see output like this:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

Notice that the logging module adds a prefix to each message, showing the log level (WARNING/DEBUG) and the module name.

Now, let's see what happens if we change the log level to only show warnings. Run the following code in the Python interpreter:

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

This time, we set the logging level to WARNING using `logging.basicConfig(level=logging.WARNING)`. Now you'll only see the WARNING messages, and the DEBUG messages will be hidden:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

This shows the advantage of using different logging levels. We can control how much detail is shown in the logs without changing our code.

To exit the Python interpreter, run the following command:

```python
exit()
```

Congratulations! You've now implemented proper exception handling and logging in your Python program. This makes your code more reliable and gives you better information when errors occur.
