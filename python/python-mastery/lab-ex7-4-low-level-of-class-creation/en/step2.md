# Creating a Typed Structure Helper

In this step, we'll build a more practical example by implementing a function that creates classes with type validation.

## Understanding the Structure Class

Open the `structure.py` file in the WebIDE editor:

```bash
cd ~/project
```

You'll notice that the `structure.py` file contains a basic `Structure` class that provides initialization and representation functionality for structured objects. Our goal is to extend this to support type validation.

## Implementing the typed_structure Function

Let's add the `typed_structure` function to `structure.py`. This function will create a new class that inherits from `Structure` and includes the specified validators:

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

Your `structure.py` file should now look like this:

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## Testing the typed_structure Function

Let's test our `typed_structure` function with the validators from the `validate.py` file. Open a Python interactive shell:

```bash
cd ~/project
python3
```

Import the necessary components and create a typed structure:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

You should see output similar to:

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

Exit the Python shell when you're done:

```python
exit()
```

This demonstrates how we can use `type()` to create custom classes with specific validation rules. This approach provides a powerful way to generate classes programmatically.
