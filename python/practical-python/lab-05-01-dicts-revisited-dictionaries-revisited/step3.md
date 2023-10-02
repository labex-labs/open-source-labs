# Dicts and Objects

User defined objects also use dictionaries for both instance data and classes. In fact, the entire object system is mostly an extra layer that's put on top of dictionaries.

A dictionary holds the instance data, `__dict__`.

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG', 'shares' : 100, 'price': 490.1 }
```

You populate this dict (and instance) when assigning to `self`.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

The instance data, `self.__dict__`, looks like this:

```python
{
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
```

**Each instance gets its own private dictionary.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

If you created 100 instances of some class, there are 100 dictionaries sitting around holding data.
