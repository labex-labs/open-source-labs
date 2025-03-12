# Adding Type Conversions

Our `MutInt` class now supports addition and comparison operations, but it still doesn't work with Python's built-in conversion functions like `int()` and `float()`. Let's add these capabilities.

1. Open `mutint.py` in the WebIDE and update it with the following code:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less-than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

We've added three new methods:

1. `__int__()`: Called when the `int()` function is used on our object
2. `__float__()`: Called when the `float()` function is used on our object
3. `__index__()`: Used for operations that specifically require an integer index, like list indexing

The `__index__` method is important for operations that specifically require an integer index, such as list indexing, slicing, and bit-length operations. We've set it to be the same as `__int__`, which is appropriate for our simple implementation.

2. Create a new test file called `test_conversions.py` to test these new methods:

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 5
print(f"\nAfter changing value to 5:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Run the test script:

```bash
python3 /home/labex/project/test_conversions.py
```

You should see output similar to this:

```
int(a): 3
float(a): 3.0
names[a]: Paula
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 5:
int(a): 5
names[a]: Lewis
```

Now our `MutInt` class can be converted to standard Python types and used in operations that require an integer index.

The `__index__` method is particularly important. It was introduced in Python to allow objects to be used in situations where an integer index is required, such as list indexing, bitwise operations, and various functions like `hex()`, `oct()`, and `bin()`.

With these additions, our `MutInt` class is now a fairly complete primitive type. It can be used in most contexts where a regular integer would be used, with the added benefit of being mutable.

## Complete MutInt Implementation

Here's our complete `MutInt` implementation with all the features we've added:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less-than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

This implementation covers the key aspects of creating a new primitive type in Python. To make it even more complete, you could implement additional methods for other operations like subtraction, multiplication, division, etc.
