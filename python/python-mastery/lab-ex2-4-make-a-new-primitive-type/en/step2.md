# Improving String Representation

When you print a `MutInt` object in Python, you'll see an output like `<__main__.MutInt object at 0x...>`. This output isn't very useful because it doesn't tell you the actual value of the `MutInt` object. To make it easier to understand what the object represents, we're going to implement special methods for string representation.

1. Open `mutint.py` in the WebIDE and update it with the following code:

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)
```

We've added three important methods to the `MutInt` class:

- `__str__()`: This method is called when you use the `str()` function on the object or when you print the object directly. It should return a human-readable string.
- `__repr__()`: This method provides the "official" string representation of the object. It's mainly used for debugging and should ideally return a string that, if passed to the `eval()` function, would recreate the object.
- `__format__()`: This method allows you to use Python's string formatting system with your `MutInt` objects. You can use format specifications like padding and number formatting.

2. Create a new test file called `test_string_repr.py` to test these new methods:

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

In this test file, we first import the `MutInt` class. Then we create a `MutInt` object with the value `3`. We test the `__str__()` and `__repr__()` methods by using the `str()` and `repr()` functions. We also test direct printing, string formatting, and the mutability of the `MutInt` object.

3. Run the test script:

```bash
python3 /home/labex/project/test_string_repr.py
```

When you run this command, Python will execute the `test_string_repr.py` script. You should see output similar to this:

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

Now our `MutInt` objects display nicely. The string representation shows the underlying value, and we can use string formatting just like with regular integers.

The difference between `__str__()` and `__repr__()` is that `__str__()` is meant to produce a human-friendly output, while `__repr__()` should ideally produce a string that, when passed to `eval()`, would recreate the object. This is why we included the class name in the `__repr__()` method.

The `__format__()` method allows our object to work with Python's formatting system, so we can use format specifications like padding and number formatting.
