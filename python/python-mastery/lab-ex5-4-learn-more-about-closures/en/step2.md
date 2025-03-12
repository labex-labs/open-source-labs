# Closures as a Code Generator

In this step, we will explore how closures can be used to generate code dynamically. Specifically, we'll implement a type-checking system for class attributes using closures.

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

This function generates a property with type checking. The `@property` decorator creates a getter for the property, and the `@value.setter` decorator creates a setter that checks the type of the value before setting it.

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
