# From Validators to Descriptors

In the previous exercise, you wrote a series of classes that could perform checking. For example:

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError('Expected %s' % cls.expected_type)
TypeError: expected <class 'int'>
>>> PositiveInteger.check(-10)
```

You can extend this to descriptors by making a simple change to the `Validator` base class. Change it to the following:

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Note: The lack of the `__get__()` method in the descriptor means that Python will use its default implementation of attribute lookup. This requires that the supplied name matches the name used in the instance dictionary.

No other changes should be necessary. Now, try modifying the `Stock` class to use the validators as descriptors like this:

```python
class Stock:
    name   = String('name')
    shares = PositiveInteger('shares')
    price  = PositiveFloat('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

You'll find that your class works the same way as before, involves much less code, and gives you all of the desired checking:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.shares = 75
>>> s.shares = '75'
... TypeError ...
>>> s.shares = -50
... ValueError ...
>>>
```

This is pretty cool. Descriptors have allowed you to greatly simplify the implementation of the `Stock` class. This is the real power of descriptors--you get low level control over the dot and can use it to do amazing things.
