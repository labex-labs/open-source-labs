# Understanding Validator Classes

In this lab, we will build upon a set of validator classes to create a callable object. Let's first understand the validator classes that have been provided in the `validate.py` file.

Open the `validate.py` file in the WebIDE:

```bash
code /home/labex/project/validate.py
```

The file contains the following classes:

1. `Validator`: A base class with a `check` method that doesn't do anything yet
2. `Typed`: A subclass of `Validator` that checks if a value is of a specific type
3. `Integer`, `Float`, and `String`: Specific type validators that inherit from `Typed`

Let's try using these validator classes to understand how they work. Create a new file called `test.py`:

```bash
code /home/labex/project/test.py
```

Add the following code to `test.py`:

```python
from validate import Integer, String, Float

# Test Integer validator
print("Testing Integer validator:")
try:
    Integer.check(42)
    print("✓ Integer check passed for 42")
except TypeError as e:
    print(f"✗ Error: {e}")

try:
    Integer.check("Hello")
    print("✗ Integer check incorrectly passed for 'Hello'")
except TypeError as e:
    print(f"✓ Correctly raised error: {e}")

# Test String validator
print("\nTesting String validator:")
try:
    String.check("Hello")
    print("✓ String check passed for 'Hello'")
except TypeError as e:
    print(f"✗ Error: {e}")
```

Run the test file:

```bash
python3 /home/labex/project/test.py
```

You should see output similar to:

```
Testing Integer validator:
✓ Integer check passed for 42
✓ Correctly raised error: Expected <class 'int'>

Testing String validator:
✓ String check passed for 'Hello'
```

These validator classes allow us to perform type checking. For example, `Integer.check(x)` will raise a `TypeError` if `x` is not an integer.

Now imagine we have a function that requires arguments of specific types:

```python
def add(x, y):
    Integer.check(x)  # Make sure x is an integer
    Integer.check(y)  # Make sure y is an integer
    return x + y
```

This works, but we need to manually add the validator checks. In the next steps, we'll create a callable object that can automatically apply these checks based on function annotations.
