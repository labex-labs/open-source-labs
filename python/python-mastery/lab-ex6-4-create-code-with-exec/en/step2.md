# Creating a Dynamic **init**() Method

Now let's apply what we've learned about `exec()` to a real-world scenario. In this step, we'll modify the `Structure` class to dynamically create an `__init__()` method based on the `_fields` class variable.

First, let's examine the existing `structure.py` file. Open it in the WebIDE:

```bash
cat /home/labex/project/structure.py
```

You should see a `Structure` class and a `Stock` class that inherits from it. The current implementation uses a manual approach to handle initialization.

Now, let's modify the `Structure` class to add a `create_init()` class method that dynamically generates an `__init__()` method. Open the `structure.py` file in the WebIDE editor and make the following changes:

1. Remove the existing `_init()` and `set_fields()` methods from the `Structure` class
2. Add the `create_init()` class method to the `Structure` class:

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

3. Modify the `Stock` class to use this new approach:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Your complete `structure.py` file should now look something like this:

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Now let's test our implementation to make sure it works correctly. Run the unit test file:

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

If your implementation is correct, you should see that all tests pass.

You can also test the class manually in the Python shell:

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

Congratulations! You've successfully used `exec()` to dynamically create an `__init__()` method based on class attributes.
