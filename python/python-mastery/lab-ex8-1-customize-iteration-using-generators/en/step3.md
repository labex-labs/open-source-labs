# Enhancing Classes with Iteration Capabilities

Now, we've made our `Structure` class and its subclasses support iteration. Iteration is a powerful concept in Python that allows you to loop through a collection of items one by one. When a class supports iteration, it becomes more flexible and can work with many built - in Python features. Let's explore how this support for iteration enables many powerful features in Python.

## Leveraging Iteration for Sequence Conversions

In Python, there are built - in functions like `list()` and `tuple()`. These functions are very useful because they can take any iterable object as an input. An iterable object is something that you can loop over, like a list, a tuple, or now, our `Structure` class instances. Since our `Structure` class now supports iteration, we can easily convert instances of it to lists or tuples.

1. Let's try these operations with a `Stock` instance. The `Stock` class is a subclass of `Structure`. Run the following command in your terminal:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

This command first imports the `Stock` class, creates an instance of it, and then converts this instance to a list and a tuple using the `list()` and `tuple()` functions respectively. The output will show you the instance represented as a list and a tuple:

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## Unpacking

Python has a very useful feature called unpacking. Unpacking allows you to take an iterable object and assign its elements to individual variables in one go. Since our `Stock` instance is iterable, we can use this unpacking feature on it.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

In this code, we create a `Stock` instance and then unpack its elements into three variables: `name`, `shares`, and `price`. Then we print these variables. The output will show the values of these variables:

```
Name: GOOG, Shares: 100, Price: 490.1
```

## Adding Comparison Capabilities

When a class supports iteration, it becomes easier to implement comparison operations. Comparison operations are used to check if two objects are equal or not. Let's add an `__eq__()` method to our `Structure` class to compare instances.

1. Open the `structure.py` file again. The `__eq__()` method is a special method in Python that is called when you use the `==` operator to compare two objects. Add the following code to the `Structure` class in the `structure.py` file:

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

This method first checks if the `other` object is an instance of the same class as `self` using the `isinstance()` function. Then it converts both `self` and `other` to tuples and checks if these tuples are equal.

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

2. After adding the `__eq__()` method, save the `structure.py` file.

3. Let's test the comparison capability. Run the following command in your terminal:

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

This code creates three `Stock` instances: `a`, `b`, and `c`. Then it compares `a` with `b` and `a` with `c` using the `==` operator. The output will show the results of these comparisons:

```
a == b: True
a == c: False
```

4. Now, to make sure everything is working correctly, we need to run the unit tests. Unit tests are a set of code that checks if different parts of your program are working as expected. Run the following command in your terminal:

```bash
python3 teststock.py
```

If everything is working correctly, you should see output indicating that the tests have passed:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

By adding just two simple methods (`__iter__()` and `__eq__()`), we've significantly enhanced our `Structure` class with capabilities that make it more Pythonic and easier to use.
