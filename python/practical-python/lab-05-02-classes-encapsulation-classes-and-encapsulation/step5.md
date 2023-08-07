# Simple Attributes

Consider the following class.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

A surprising feature is that you can set the attributes to any value at all:

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

You might look at that and think you want some extra checks.

```python
s.shares = '50'     # Raise a TypeError, this is a string
```

How would you do it?
