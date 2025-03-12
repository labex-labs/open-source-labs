# Applying Function Inspection in Classes

Now, we're going to take what we've learned about function inspection and use it to improve a class implementation. Function inspection allows us to look inside functions and understand their structure, like the parameters they take. In this case, we'll use it to make our class code more efficient and less error - prone. We'll modify a `Structure` class so that it can automatically detect field names from the `__init__` method signature.

## Understanding the Structure Class

The `structure.py` file contains a `Structure` class. This class acts as a base class, which means other classes can inherit from it to create structured data objects. Currently, to define the attributes of the objects created from classes inheriting from `Structure`, we need to set a `_fields` class variable.

Let's open the file in the editor. We'll use the following command to navigate to the project directory:

```bash
cd ~/project
```

Once you've run this command, you can find and view the existing `Structure` class in the `structure.py` file within the WebIDE.

## Creating a Stock Class

Let's create a `Stock` class that inherits from the `Structure` class. Inheritance means that the `Stock` class will get all the features of the `Structure` class and can also add its own. We'll add the following code to the end of the `structure.py` file:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

However, there's a problem with this approach. We have to define both the `_fields` tuple and the `__init__` method with the same parameter names. This is redundant because we're essentially writing the same information twice. If we forget to update one when we change the other, it can lead to errors.

## Adding a set_fields Class Method

To fix this issue, we'll add a `set_fields` class method to the `Structure` class. This method will automatically detect the field names from the `__init__` signature. Here's the code we need to add to the `Structure` class:

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

This method uses the `inspect` module, which is a powerful tool in Python for getting information about objects like functions and classes. First, it gets the signature of the `__init__` method. Then, it extracts the parameter names, but skips the `self` parameter because `self` is a special parameter in Python classes that refers to the instance itself. Finally, it sets the `_fields` class variable with these parameter names.

## Modifying the Stock Class

Now that we have the `set_fields` method, we can simplify our `Stock` class. Replace the previous `Stock` class code with the following:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

This way, we don't have to manually define the `_fields` tuple. The `set_fields` method will take care of it for us.

## Testing the Modified Class

To make sure our modified class works correctly, we'll create a simple test script. Create a new file called `test_structure.py` and add the following code:

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

This test script creates a `Stock` object, tests its string representation, accesses its attributes, modifies an attribute, and tries to access a misspelled attribute to check if it raises the correct error.

To run the test script, use the following command:

```bash
python3 test_structure.py
```

You should see output similar to this:

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## How It Works

1. The `set_fields` method uses `inspect.signature()` to get the parameter names from the `__init__` method. This function gives us detailed information about the parameters of the `__init__` method.
2. It then automatically sets the `_fields` class variable based on these parameter names. So, we don't have to write the same parameter names in two different places.
3. This eliminates the need to manually define both `_fields` and `__init__` with matching parameter names. It makes our code more maintainable because if we change the parameters in the `__init__` method, the `_fields` will be updated automatically.

This approach uses function inspection to make our code more maintainable and less error - prone. It's a practical application of Python's introspection capabilities, which allow us to examine and modify objects at runtime.
