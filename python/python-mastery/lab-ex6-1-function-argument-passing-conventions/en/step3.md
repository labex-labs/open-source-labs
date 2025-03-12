# Improving Object Representation

Our `Structure` class works for creating and accessing objects, but it lacks a good string representation. When we print objects or see them in the Python interpreter, we want a clear and informative display.

## Understanding Python's Object Representation

Python provides two special methods for object representation:

- `__str__` - Used by `str()` and `print()` for a human-readable representation
- `__repr__` - Used by the interpreter and `repr()` for a more technical, unambiguous representation

Let's add a `__repr__` method to our `Structure` class to make debugging easier.

## Implementing a Good Representation

Update your `structure.py` file by adding the `__repr__` method to the `Structure` class:

```python
def __repr__(self):
    """
    Return a representation of the object that can be used to recreate it.
    Example: Stock('GOOG', 100, 490.1)
    """
    # Get the class name
    cls_name = type(self).__name__

    # Get all the field values
    values = [getattr(self, name) for name in self._fields]

    # Format the fields and values
    args_str = ', '.join(repr(value) for value in values)

    # Return the formatted string
    return f"{cls_name}({args_str})"
```

This method:

1. Gets the class name using `type(self).__name__`
2. Retrieves all the field values from the instance
3. Creates a string representation with the class name and values

## Testing the Improved Representation

Let's test our enhanced implementation. Create a new file called `test_repr.py`:

```python
# test_repr.py
from structure import Stock, Point, Date

# Create instances
s = Stock('GOOG', 100, 490.1)
p = Point(3, 4)
d = Date(2023, 11, 9)

# Print the representations
print(repr(s))
print(repr(p))
print(repr(d))

# Direct printing also uses __repr__ in the interpreter
print(s)
print(p)
print(d)
```

Run the test:

```bash
python3 test_repr.py
```

Expected output:

```
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
```

This output is much more informative! When we see `Stock('GOOG', 100, 490.1)`, we immediately understand what the object represents, and we could even recreate it by copying this representation.

## The Benefit of Good Representations

A good `__repr__` implementation makes debugging much easier. When you're inspecting objects in the interpreter or logging them during program execution, having a clear representation helps identify issues quickly.
