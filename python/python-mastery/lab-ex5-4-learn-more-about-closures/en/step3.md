# Eliminating Property Names with Descriptors

In the previous step, when creating typed properties, we had to explicitly state the property names. This is redundant because the property names are already specified in the class definition. In this step, we'll use descriptors to get rid of this redundancy.

A descriptor in Python is a special object that controls how attribute access works. When you implement the `__set_name__` method in a descriptor, it can automatically grab the attribute name from the class definition.

Let's start by creating a new file.

1. Create a new file named `improved_typedproperty.py` with the following code:

```python
# improved_typedproperty.py

class TypedProperty:
    """
    A descriptor that performs type checking.

    This descriptor automatically captures the attribute name from the class definition.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Convenience functions
def String():
    """Create a string property with type checking."""
    return TypedProperty(str)

def Integer():
    """Create an integer property with type checking."""
    return TypedProperty(int)

def Float():
    """Create a float property with type checking."""
    return TypedProperty(float)
```

This code defines a descriptor class called `TypedProperty` that checks the type of values assigned to attributes. The `__set_name__` method is called automatically when the descriptor is assigned to a class attribute. This allows the descriptor to capture the attribute name without us having to specify it manually.

Next, we'll create a class that uses these improved typed properties.

2. Create a new file named `stock_improved.py` that uses the improved typed properties:

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    # No need to specify property names anymore
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Notice that we don't need to specify the property names when creating the typed properties. The descriptor will automatically get the attribute name from the class definition.

Now, let's test our improved class.

3. Create a test file `test_stock_improved.py` to test the improved version:

```python
from stock_improved import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try setting attributes with wrong types
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

Finally, we'll run the test to see if everything works as expected.

4. Run the test:

```bash
python3 test_stock_improved.py
```

You should see output similar to:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

In this step, we've made our type-checking system better by using descriptors and the `__set_name__` method. This gets rid of the redundant property name specification, making the code shorter and less likely to have errors.

The `__set_name__` method is a very useful feature of descriptors. It lets them automatically gather information about how they're used in a class definition. This can be used to create APIs that are easier to understand and use.
