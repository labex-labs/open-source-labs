# Handling More Complex Patterns

Our current function works for camelCase, but we need to enhance it to handle additional patterns like:

1. PascalCase (e.g., `HelloWorld`)
2. Strings with hyphens (e.g., `hello-world`)
3. Strings that already have underscores (e.g., `hello_world`)

Let's update our function to handle these cases:

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

The enhancements we made:

1. First, we replace any hyphens with spaces.
2. The new regex `re.sub('([A-Z]+)', r' \1', s)` adds a space before any sequence of uppercase letters, which helps with PascalCase.
3. We keep our camelCase handling regex.
4. Finally, we split the string by spaces, join with underscores, and convert to lowercase, which handles any remaining spaces and ensures consistent output.

Run your script to test with various input formats:

```bash
python3 ~/project/snake_case.py
```

You should see output like:

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

Our function is now more robust and can handle various input formats. In the next step, we'll make our final refinements and test against the full test suite.
