# Creating a Typed Structure Helper

In this step, we're going to build a more practical example. We'll implement a function that creates classes with type validation. Type validation is crucial as it ensures that the data assigned to class attributes meets specific criteria, like being a certain data type or within a particular range. This helps catch errors early and makes our code more robust.

## Understanding the Structure Class

First, we need to open the `structure.py` file in the WebIDE editor. This file contains a basic `Structure` class. This class provides the fundamental functionality for initializing and representing structured objects. Initialization means setting up the object with the provided data, and representation is about how the object is displayed when we print it.

To open the file, we'll use the following command in the terminal:

```bash
cd ~/project
```

After running this command, you'll be in the correct directory where the `structure.py` file is located. When you open the file, you'll notice the basic `Structure` class. Our goal is to extend this class to support type validation.

## Implementing the typed_structure Function

Now, let's add the `typed_structure` function to the `structure.py` file. This function will create a new class that inherits from the `Structure` class and includes the specified validators. Inheritance means that the new class will have all the functionality of the `Structure` class and can also add its own features. Validators are used to check if the values assigned to the class attributes are valid.

Here's the code for the `typed_structure` function:

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

The `clsname` parameter is the name we want to give to the new class. The `validators` parameter is a dictionary where the keys are the attribute names and the values are the validator objects. The `type()` function is used to create a new class dynamically. It takes three arguments: the class name, a tuple of base classes (in this case, just the `Structure` class), and a dictionary of class attributes (the validators).

After adding this function, your `structure.py` file should look like this:

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

Let's test our `typed_structure` function using the validators from the `validate.py` file. These validators are used to check if the values assigned to the class attributes are of the correct type and meet other criteria.

First, open a Python interactive shell. We'll use the following commands in the terminal:

```bash
cd ~/project
python3
```

The first command takes us to the correct directory, and the second command starts the Python interactive shell.

Now, import the necessary components and create a typed structure:

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

We import the `String`, `PositiveInteger`, and `PositiveFloat` validators from the `validate.py` file. Then we use the `typed_structure` function to create a `Stock` class with type validation. We create an instance of the `Stock` class and test it by printing its attributes. Finally, we try to create an invalid stock instance to test the validation.

You should see output similar to:

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

When you're done testing, exit the Python shell:

```python
exit()
```

This example demonstrates how we can use the `type()` function to create custom classes with specific validation rules. This approach is very powerful as it allows us to generate classes programmatically, which can save a lot of time and make our code more flexible.
