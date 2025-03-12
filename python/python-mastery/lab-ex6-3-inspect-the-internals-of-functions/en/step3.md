# Applying Function Inspection in Classes

Now, let's apply what we've learned about function inspection to improve a class implementation. We'll modify a `Structure` class to automatically detect field names from the `__init__` method signature.

## Understanding the Structure Class

The `structure.py` file contains a `Structure` class that serves as a base class for creating structured data objects. It currently requires a `_fields` class variable to define the object's attributes:

Open the file in the editor:

```bash
cd ~/project
```

You can see the existing `Structure` class in the `structure.py` file in the WebIDE.

## Creating a Stock Class

Let's create a `Stock` class that inherits from `Structure`. Add this code to the end of the `structure.py` file:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

The problem with this approach is that we have to define both the `_fields` tuple and the `__init__` method with the same parameter names, which is redundant and could lead to errors if they get out of sync.

## Adding a set_fields Class Method

Let's improve this by adding a `set_fields` class method to `Structure` that automatically detects field names from the `__init__` signature. Add this method to the `Structure` class:

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

This method uses the `inspect` module to get the signature of the `__init__` method, extracts the parameter names (skipping `self`), and sets the `_fields` class variable.

## Modifying the Stock Class

Now we can simplify our `Stock` class. Replace the previous `Stock` class with:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

## Testing the Modified Class

Let's create a simple test script to verify that our modified class works correctly. Create a new file called `test_structure.py`:

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

Run the test script:

```bash
python3 test_structure.py
```

You should see output similar to:

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## How It Works

1. The `set_fields` method uses `inspect.signature()` to get the parameter names from the `__init__` method.
2. It automatically sets the `_fields` class variable based on these parameter names.
3. This eliminates the need to manually define both `_fields` and `__init__` with matching parameter names.

This approach uses function inspection to make our code more maintainable and less error-prone. It's a practical application of Python's introspection capabilities.
