# Implementing the Advanced Initialization in Structure

We've just learned two powerful techniques for accessing function arguments. Now, we'll use these techniques to update our `Structure` class. First, let's understand why we're doing this. These techniques will make our class more flexible and easier to use, especially when dealing with different types of arguments.

Open the `structure.py` file in the code editor. You can do this by running the following commands in the terminal. The `cd` command changes the directory to the project folder, and the `code` command opens the `structure.py` file in the code editor.

```bash
cd ~/project
code structure.py
```

Replace the content of the file with the following code. This code defines a `Structure` class with several methods. Let's go through each part to understand what it does.

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

Here's what we've done in the code:

1. We removed the old `__init__()` method. Since subclasses will define their own `__init__` methods, we don't need the old one anymore.
2. We added a new `_init()` static method. This method uses frame inspection to automatically capture and set all parameters as attributes. Frame inspection allows us to access the local variables of the calling method.
3. We kept the `__repr__()` method. This method provides a nice string representation of the object, which is useful for debugging and printing.
4. We added a `__setattr__()` method. This method enforces attribute validation, ensuring that only valid attributes can be set on the object.

Now, let's update the `Stock` class. Open the `stock.py` file using the following command:

```bash
code stock.py
```

Replace its content with the following code:

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

The key change here is that our `__init__` method now calls `self._init()` instead of manually setting each attribute. The `_init()` method uses frame inspection to automatically capture and set all parameters as attributes. This makes the code more concise and easier to maintain.

Let's test our implementation by running the unit tests. The unit tests will help us ensure that our code works as expected. Run the following commands in the terminal:

```bash
cd ~/project
python3 teststock.py
```

You should see that all tests pass, including the test for keyword arguments that failed before. This means our implementation is working correctly.

Let's also check the help documentation for our `Stock` class. The help documentation provides information about the class and its methods. Run the following command in the terminal:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Now you should see a proper signature for the `__init__` method, showing all the parameter names. This makes it easier for other developers to understand how to use the class.

Finally, let's interactively test that keyword arguments work as expected. Run the following command in the terminal:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

You should see the Stock object properly created with the specified attributes. This confirms that our class initialization system supports keyword arguments.

With this implementation, we've achieved a much more flexible and user-friendly class initialization system that:

1. Preserves proper function signatures in documentation, making it easier for developers to understand how to use the class.
2. Supports both positional and keyword arguments, providing more flexibility when creating objects.
3. Requires minimal boilerplate code in subclasses, reducing the amount of code you need to write.
