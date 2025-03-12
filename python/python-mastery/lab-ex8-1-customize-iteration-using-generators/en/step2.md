# Adding Iteration to Custom Classes

Now that you understand the basics of generators, let's use them to add iteration capabilities to custom classes. In Python, making a class iterable involves implementing the `__iter__()` special method.

## Understanding the `__iter__()` Method

The `__iter__()` method should return an iterator object. A simple way to do this is to define `__iter__()` as a generator function that yields the values you want to iterate over.

## Modifying the Structure Class

In the setup for this lab, we provided a base `Structure` class that other classes like `Stock` can inherit from. Let's add an `__iter__()` method to this class to make all subclasses iterable.

1. Open the file `structure.py` in the WebIDE:

```bash
cd ~/project
```

2. Look at the current implementation of the `Structure` class:

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

3. Add an `__iter__()` method that yields each attribute value in order:

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
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
```

4. Save the file.

5. Now let's test the iteration capability by creating a `Stock` instance and iterating over it:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

You should see output like this:

```
Iterating over Stock:
GOOG
100
490.1
```

Now any class that inherits from `Structure` will automatically be iterable, and iteration will yield the attribute values in the order defined by the `_fields` list.
