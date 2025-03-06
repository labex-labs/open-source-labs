# Understanding the Problem

Before we write our snake case conversion function, let's understand what we need to accomplish:

1. We need to convert a string from any format to snake case
2. Snake case means all lowercase letters with underscores between words
3. We need to handle different input formats:
   - camelCase (e.g., `camelCase` → `camel_case`)
   - Strings with spaces (e.g., `some text` → `some_text`)
   - Strings with mixed formatting (e.g., hyphens, underscores, and mixed case)

Let's start by creating a new Python file for our snake case function. In the WebIDE, navigate to the project directory and create a new file called `snake_case.py`:

```python
# This function will convert a string to snake case
def snake(s):
    # We'll implement this function step by step
    pass  # Placeholder for now

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Save this file. In the next step, we'll start implementing the function.

For now, let's run our placeholder function to make sure our file is set up correctly. Open a terminal and run:

```bash
python3 ~/project/snake_case.py
```

![python-prompt](../assets/screenshot-20250306-B5lI9tyo@2x.png)

You should see an output like:

```
Original: helloWorld
Snake case: None
```

The result is `None` because our function is currently just returning the default Python `None` value. In the next step, we'll add the actual conversion logic.
