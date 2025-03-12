# Improving String Representation

When we print our `MutInt` object, Python displays it as `<__main__.MutInt object at 0x...>`, which is not very helpful. Let's improve how our object is displayed by implementing special methods for string representation.

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

We've added three important methods:

- `__str__()`: Used when `str()` is called on the object or when it's printed
- `__repr__()`: Used for the "official" string representation of the object
- `__format__()`: Used when the object is formatted with the `format()` function or f-strings

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

3. Run the test script:

```bash
python3 /home/labex/project/test_string_repr.py
```

You should see output similar to this:

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
