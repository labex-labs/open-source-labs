# Understanding the Problem with Class Initialization

In previous exercises, you may have created a `Structure` class that helps define data structures easily. This base class handles the initialization of attributes based on a predefined list of field names.

Let's examine the current implementation. Open the `structure.py` file in the code editor to review its content:

```bash
cd ~/project
code structure.py
```

The `Structure` class provides a framework for defining simple data structures. When we create a subclass like `Stock`, we define the fields we want:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
```

Now, open the `stock.py` file to see the current implementation:

```bash
code stock.py
```

This approach works, but it has several limitations. Let's identify these issues by running the Python interpreter and exploring the behavior:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

You'll notice that the signature shown in the help output isn't very useful - it only shows `*args` instead of the actual parameter names.

Let's also try to create a `Stock` instance using keyword arguments:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

You should get an error like:

```
TypeError: __init__() got an unexpected keyword argument 'name'
```

This happens because our current `__init__` method doesn't handle keyword arguments - it only accepts positional arguments. This is a limitation we want to fix.

In this lab, we'll explore different approaches to make our `Structure` class more flexible and user-friendly.
