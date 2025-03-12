# Adding Mathematical Operations

Currently, our `MutInt` class doesn't support mathematical operations like addition. In Python, to enable such operations for a custom class, we need to implement special methods. These special methods are also known as "magic methods" or "dunder methods" because they are surrounded by double underscores. Let's add the functionality for addition by implementing the relevant special methods for arithmetic operations.

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
        # For commutative operations like +, we can reuse __add__
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
```

We've added three new methods to the `MutInt` class:

- `__add__()`: This method is called when the `+` operator is used with our `MutInt` object on the left side. Inside this method, we first check if the `other` operand is an instance of `MutInt` or an `int`. If it is, we perform the addition and return a new `MutInt` object with the result. If the `other` operand is something else, we return `NotImplemented`. This tells Python to try other methods or raise a `TypeError`.
- `__radd__()`: This method is called when the `+` operator is used with our `MutInt` object on the right side. Since addition is a commutative operation (i.e., `a + b` is the same as `b + a`), we can simply reuse the `__add__` method.
- `__iadd__()`: This method is called when the `+=` operator is used on our `MutInt` object. Instead of creating a new object, it modifies the existing `MutInt` object and returns it.

2. Create a new test file called `test_math_ops.py` to test these new methods:

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

In this test file, we first import the `MutInt` class. Then we create some `MutInt` objects and perform different types of addition operations. We also test the in-place addition and the case where an unsupported operation (adding a float) is attempted.

3. Run the test script:

```bash
python3 /home/labex/project/test_math_ops.py
```

You should see output similar to this:

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

Now our `MutInt` class supports basic addition operations. Notice that when we used `+=`, both `a` and `f` were updated. This shows that `a += 10` modified the existing object rather than creating a new one.

This behavior with mutable objects is similar to Python's built-in mutable types like lists. For example:

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

In contrast, for immutable types like tuples, `+=` creates a new object:

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
