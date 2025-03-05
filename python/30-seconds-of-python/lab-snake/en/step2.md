# Using Regular Expressions for Pattern Matching

To convert strings to snake case, we'll use regular expressions (regex) to identify word boundaries. The `re` module in Python provides powerful pattern matching capabilities that we can use for this task.

Let's update our function to handle camelCase strings:

1. First, we need to identify the pattern where a lowercase letter is followed by an uppercase letter (like in "camelCase")
2. Then, we'll insert a space between them
3. Finally, we'll convert everything to lowercase and replace spaces with underscores

Update your `snake_case.py` file with this improved function:

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Let's break down what this function does:

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)` looks for patterns where a lowercase letter `([a-z])` is followed by an uppercase letter `([A-Z])`. It then replaces this pattern with the same letters but adds a space between them using `\1` and `\2` which refer to the captured groups.
- Then we convert everything to lowercase with `lower()` and replace spaces with underscores.

Run your script again to see if it works for camelCase:

```bash
python3 ~/project/snake_case.py
```

The output should now be:

```
Original: helloWorld
Snake case: hello_world
```

Great! Our function can now handle camelCase strings. In the next step, we'll enhance it to handle more complex cases.
