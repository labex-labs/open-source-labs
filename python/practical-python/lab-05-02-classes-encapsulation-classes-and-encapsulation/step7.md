# Properties

There is an alternative approach to the previous pattern.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

Normal attribute access now triggers the getter and setter methods
under `@property` and `@shares.setter`.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Triggers @property
50
>>> s.shares = 75    # Triggers @shares.setter
>>>
```

With this pattern, there are _no changes_ needed to the source code.
The new _setter_ is also called when there is an assignment within the class,
including inside the `__init__()` method.

```python
class Stock:
    def __init__(self, name, shares, price):
        ...
        # This assignment calls the setter below
        self.shares = shares
        ...

    ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

There is often a confusion between a property and the use of private names.
Although a property internally uses a private name like `_shares`, the rest
of the class (not the property) can continue to use a name like `shares`.

Properties are also useful for computed data attributes.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    ...
```

This allows you to drop the extra parentheses, hiding the fact that it's actually a method:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # Instance variable
100
>>> s.cost   # Computed Value
49010.0
>>>
```
