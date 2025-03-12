# Enhancing Classes with Iteration Capabilities

Now that our `Structure` class and its subclasses support iteration, let's explore how this enables many powerful features in Python.

## Leveraging Iteration for Sequence Conversions

Python's built-in functions like `list()` and `tuple()` work with any iterable object. Since our `Structure` class now supports iteration, we can easily convert instances to lists or tuples:

1. Try these operations with a `Stock` instance:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

Output:

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## Unpacking

Python's unpacking feature also works with iterables. You can unpack a `Stock` instance directly into variables:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

Output:

```
Name: GOOG, Shares: 100, Price: 490.1
```

## Adding Comparison Capabilities

With iteration support, we can now easily implement comparison operations. Let's add an `__eq__()` method to our `Structure` class to compare instances:

1. Open `structure.py` again and add the `__eq__()` method:

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

The complete `structure.py` file should now look like this:

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. Save the file.

3. Let's test the comparison capability:

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

Output:

```
a == b: True
a == c: False
```

4. Now run the unit tests to make sure everything is working correctly:

```bash
python3 teststock.py
```

You should see output indicating that the tests have passed:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

By adding just two simple methods (`__iter__()` and `__eq__()`), we've significantly enhanced our `Structure` class with capabilities that make it more Pythonic and easier to use.
