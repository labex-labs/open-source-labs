# Returning Optional Values

Sometimes a function might encounter situations where it cannot produce a valid result. In such cases, it's common in Python to return `None` to indicate the absence of a valid return value.

Let's modify our `parse_line` function to handle cases where the input string is not in the expected format.

1. Update the `parse_line` function in your `return_values.py` file:

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.
    If the line is not in the correct format, return None.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple or None: A tuple containing (name, value) or None if parsing failed
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
    else:
        return None  # Return None for invalid input
```

2. Add test code to demonstrate the updated function:

```python
# Test the updated parse_line function
if __name__ == "__main__":
    # Valid input
    result1 = parse_line('email=guido@python.org')
    print(f"Valid input result: {result1}")

    # Invalid input
    result2 = parse_line('invalid_line_without_equals_sign')
    print(f"Invalid input result: {result2}")

    # Checking for None before using the result
    test_line = 'user_info'
    result = parse_line(test_line)
    if result is None:
        print(f"Could not parse the line: '{test_line}'")
    else:
        name, value = result
        print(f"Name: {name}, Value: {value}")
```

3. Save the file and run it:

```
python ~/project/return_values.py
```

You should see output similar to:

```
Valid input result: ('email', 'guido@python.org')
Invalid input result: None
Could not parse the line: 'user_info'
```

**Explanation:**

- The function now checks if the line contains an equals sign
- If not, it returns `None` to indicate that parsing failed
- When using such a function, it's important to check if the result is `None` before trying to use it

**Design Discussion:**
An alternative approach would be to raise an exception when the input is invalid. This would be appropriate if:

1. Invalid input is truly exceptional and not an expected case
2. You want to force the caller to handle the error
3. You need to provide detailed error information

Example of an exception-based approach:

```python
def parse_line_with_exception(line):
    """Parse a line and raise an exception for invalid input."""
    parts = line.split('=', 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid format: '{line}' does not contain '='")
    return (parts[0], parts[1])
```

The choice between returning `None` and raising exceptions depends on your application's needs:

- Return `None` when the absence of a result is common and expected
- Raise exceptions when the failure is unexpected and should interrupt normal flow
