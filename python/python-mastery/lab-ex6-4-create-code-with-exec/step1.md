# Experiment with exec()

Define a fragment of Python code in a string and try running it:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
>>>
```

That's interesting, but executing random code fragments is not especially useful. A more interesting use of `exec()` is in making code such as functions, methods, or classes. Try this example in which we make an `__init__()` function for a class.

```python
>>> class Stock:
        _fields = ('name', 'shares', 'price')

>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
        code += f'    self.{name} = {name}\n'
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
>>>
```

In this example, an `__init__()` function is made directly from the `_fields` variable.\
There are no weird hacks involving a special `_init()` method or stack frames.
