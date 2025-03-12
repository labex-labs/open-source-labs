# Creating a Dynamic **init**() Method

Now, we're going to apply what we've learned about the `exec()` function to a real - world programming scenario. In Python, the `exec()` function allows you to execute Python code stored in a string. In this step, we'll modify the `Structure` class to dynamically create an `__init__()` method. The `__init__()` method is a special method in Python classes, which is called when an object of the class is instantiated. We'll base the creation of this method on the `_fields` class variable, which contains a list of field names for the class.

First, let's take a look at the existing `structure.py` file. This file contains the current implementation of the `Structure` class and a `Stock` class that inherits from it. To view the contents of the file, open it in the WebIDE using the following command:

```bash
cat /home/labex/project/structure.py
```

In the output, you'll see that the current implementation uses a manual approach to handle the initialization of objects. This means that the code for initializing the object's attributes is written explicitly, rather than being generated dynamically.

Now, we're going to modify the `Structure` class. We'll add a `create_init()` class method that will dynamically generate the `__init__()` method. To make these changes, open the `structure.py` file in the WebIDE editor and follow these steps:

1. Remove the existing `_init()` and `set_fields()` methods from the `Structure` class. These methods are part of the manual initialization approach, and we won't need them anymore since we're going to use a dynamic approach.

2. Add the `create_init()` class method to the `Structure` class. Here's the code for the method:

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

In this method, we first create a string `argstr` that contains all the field names separated by commas. This string will be used as the argument list for the `__init__()` method. Then, we create the code for the `__init__()` method as a string. We loop through the field names and add lines to the code that assign each argument to the corresponding object attribute. After that, we use the `exec()` function to execute the code and store the generated function in the `locs` dictionary. Finally, we use the `setattr()` function to set the generated function as the `__init__()` method of the class.

3. Modify the `Stock` class to use this new approach:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Here, we define the `_fields` for the `Stock` class and then call the `create_init()` method to generate the `__init__()` method for the `Stock` class.

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

Now, let's test our implementation to make sure it works correctly. We'll run the unit test file to check if all the tests pass. Use the following commands:

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

If your implementation is correct, you should see that all tests pass. This means that the dynamically generated `__init__()` method is working as expected.

You can also test the class manually in the Python shell. Here's how you can do it:

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

In the Python shell, we first import the `Stock` class from the `structure.py` file. Then, we create an instance of the `Stock` class and print it. We can also modify the `shares` attribute of the object. However, when we try to set an attribute that doesn't exist in the `_fields` list, we should get an `AttributeError`.

Congratulations! You've successfully used the `exec()` function to dynamically create an `__init__()` method based on class attributes. This approach can make your code more flexible and easier to maintain, especially when dealing with classes that have a variable number of attributes.
