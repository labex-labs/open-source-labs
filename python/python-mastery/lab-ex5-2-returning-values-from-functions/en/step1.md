# Returning Multiple Values from Functions

When a function needs to return more than one value, Python offers a convenient solution: returning a tuple. A tuple is an immutable sequence type that can hold multiple values.

Let's create a function to parse configuration lines in the format `name=value`, which returns both the name and value as separate items.

1. Create a new Python file named `return_values.py` in the project directory:

```
touch ~/project/return_values.py
```

2. Open the file in the editor and write the `parse_line` function:

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple: A tuple containing (name, value)
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
```

3. Add some test code to demonstrate the function:

```python
# Test the parse_line function
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Unpacking the tuple into separate variables
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

4. Save the file and run it from the terminal:

```
python ~/project/return_values.py
```

You should see output similar to:

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**Explanation:**

- The function splits the input string at the '=' character
- It returns both parts as a tuple using the syntax `return (name, value)`
- When calling the function, you can either store the entire tuple in one variable or "unpack" it directly into separate variables using the syntax `name, value = parse_line(...)`

This pattern of returning multiple values as a tuple is very common in Python and makes functions more versatile when they need to provide more than one piece of information to the caller.
