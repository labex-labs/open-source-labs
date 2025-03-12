# Creating a Structure Base Class

Now that we understand function argument passing, let's create a reusable base class for data structures. This will reduce code duplication when creating simple data-holding classes.

## The Problem with Repetitive Code

In earlier exercises, you defined a `Stock` class like this:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Notice how repetitive the `__init__` method is - you're writing each attribute assignment manually. This becomes tedious when you have many such classes with numerous attributes.

## Creating a Flexible Base Class

Let's create a `Structure` base class that automatically handles attribute assignment. Create a new file named `structure.py` in the WebIDE and add the following code:

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

This base class:

1. Defines a `_fields` class variable (empty by default)
2. Checks that the number of arguments matches the number of fields
3. Sets attributes using the field names and provided values

## Testing Our Structure Base Class

Now let's create some example classes that inherit from `Structure`. Add these to your `structure.py` file:

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

To test our implementation, let's create a test file named `test_structure.py`:

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

Run the test file to see if our implementation works:

```bash
python3 test_structure.py
```

Expected output:

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

Our base class is working correctly! It's now much easier to define new data structures without repeating boilerplate code.
