# Understanding the Basics of exec()

The `exec()` function in Python allows you to execute dynamically created code at runtime. This is particularly useful when you need to generate code based on some input or configuration.

Let's experiment with the basic usage of `exec()` by opening a Python shell. Open your terminal and type `python3` to start the interactive Python interpreter:

```bash
python3
```

Now, let's define a fragment of Python code as a string and execute it using `exec()`:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

In this example:

1. We defined a string `code` containing a Python for-loop
2. We defined a variable `n` with value 10
3. We executed the code using `exec(code)`
4. The loop printed the numbers 0 through 9

The power of `exec()` becomes more evident when we use it to create more complex code structures like functions or methods. Let's try a more advanced example where we dynamically create an `__init__()` method for a class:

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

In this more complex example:

1. We defined a `Stock` class with a `_fields` attribute
2. We created a string containing Python code for an `__init__` method
3. We executed this code using `exec()` and stored the resulting function in a dictionary
4. We assigned this function as the `__init__` method of our class
5. We created an instance of `Stock` and verified that the method works correctly

This demonstrates how `exec()` can be used to dynamically create methods based on data available at runtime.
