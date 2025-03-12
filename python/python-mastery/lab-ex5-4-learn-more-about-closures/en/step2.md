# Closures as a Code Generator

In this step, we'll learn how closures can be used to generate code dynamically. Specifically, we'll build a type-checking system for class attributes using closures.

First, let's understand what closures are. A closure is a function object that remembers values in the enclosing scope even if they are not present in memory. In Python, closures are created when a nested function references a value from its enclosing function.

Now, we'll start implementing our type-checking system.

1. Create a new file named `typedproperty.py` in the `/home/labex/project` directory with the following code:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Create a property with type checking.

    Args:
        name: The name of the property
        expected_type: The expected type of the property value

    Returns:
        A property object that performs type checking
    """
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

In this code, the `typedproperty` function is a closure. It takes two arguments: `name` and `expected_type`. The `@property` decorator is used to create a getter method for the property, which retrieves the value of the private attribute. The `@value.setter` decorator creates a setter method that checks if the value being set is of the expected type. If not, it raises a `TypeError`.

2. Now let's create a class that uses these typed properties. Create a file named `stock.py` with the following code:

```python
from typedproperty import typedproperty

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

In the `Stock` class, we use the `typedproperty` function to create type-checked attributes for `name`, `shares`, and `price`. When we create an instance of the `Stock` class, the type checking will be applied automatically.

3. Let's create a test file to see this in action. Create a file named `test_stock.py` with the following code:

```python
from stock import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

In this test file, we first create a `Stock` object with correct types. Then we try to set the `shares` attribute to a string, which should raise a `TypeError` because the expected type is an integer.

4. Run the test file:

```bash
python3 test_stock.py
```

You should see output similar to:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

This output shows that the type checking is working correctly.

5. Now, let's enhance `typedproperty.py` by adding convenience functions for common types. Add the following code to the end of the file:

```python
def String(name):
    """Create a string property with type checking."""
    return typedproperty(name, str)

def Integer(name):
    """Create an integer property with type checking."""
    return typedproperty(name, int)

def Float(name):
    """Create a float property with type checking."""
    return typedproperty(name, float)
```

These functions are just wrappers around the `typedproperty` function, making it easier to create properties of common types.

6. Create a new file named `stock_enhanced.py` that uses these convenience functions:

```python
from typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

This `Stock` class uses the convenience functions to create type-checked attributes, which makes the code more readable.

7. Create a test file `test_stock_enhanced.py` to test the enhanced version:

```python
from stock_enhanced import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

This test file is similar to the previous one, but it tests the enhanced `Stock` class.

8. Run the test:

```bash
python3 test_stock_enhanced.py
```

You should see output similar to:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

In this step, we've demonstrated how closures can be used to generate code. The `typedproperty` function creates property objects that perform type checking, and the `String`, `Integer`, and `Float` functions create specialized properties for common types.
