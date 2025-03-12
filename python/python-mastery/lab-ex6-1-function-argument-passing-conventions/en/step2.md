# Creating a Structure Base Class

Now that we have a good understanding of function argument passing, we're going to create a reusable base class for data structures. This step is crucial because it helps us avoid writing the same code over and over again when we create simple classes that hold data. By using a base class, we can streamline our code and make it more efficient.

## The Problem with Repetitive Code

In the earlier exercises, you defined a `Stock` class as shown below:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Take a close look at the `__init__` method. You'll notice that it's quite repetitive. You have to manually assign each attribute one by one. This can become very tedious and time - consuming, especially when you have many classes with a large number of attributes.

## Creating a Flexible Base Class

Let's create a `Structure` base class that can automatically handle attribute assignment. First, open the WebIDE and create a new file named `structure.py`. Then, add the following code to this file:

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

This base class has several important features:

1. It defines a `_fields` class variable. By default, this variable is empty. This variable will hold the names of the attributes that the class will have.
2. It checks if the number of arguments passed to the constructor matches the number of fields defined in `_fields`. If they don't match, it raises a `TypeError`. This helps us catch errors early.
3. It sets the attributes of the object using the field names and the values provided as arguments. The `setattr` function is used to dynamically set the attributes.

## Testing Our Structure Base Class

Now, let's create some example classes that inherit from the `Structure` base class. Add the following code to your `structure.py` file:

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

To test if our implementation works correctly, we'll create a test file named `test_structure.py`. Add the following code to this file:

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

To run the test, open your terminal and execute the following command:

```bash
python3 test_structure.py
```

You should see the following output:

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

As you can see, our base class is working as expected. It has made it much easier to define new data structures without having to write the same boilerplate code repeatedly.
