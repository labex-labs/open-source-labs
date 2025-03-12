# Understanding the Descriptor Protocol

In this step, we will create a simple `Stock` class that demonstrates how descriptors work in Python. The descriptor protocol consists of three special methods: `__get__()`, `__set__()`, and `__delete__()`.

First, create a new file called `stock.py` in the project directory:

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

Now, open a Python shell to experiment with the `Stock` class and see descriptors in action:

```bash
cd ~/project
python3 -i stock.py
```

In the Python shell, create a stock object and try accessing its attributes:

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

The `property` decorators in our class are actually using descriptors behind the scenes. Let's examine the class dictionary to see the descriptor objects:

```python
Stock.__dict__.keys()
```

You should see output similar to this:

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

Now we can examine how descriptors work by manually calling their methods:

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

When you access attributes like `s.shares`, Python calls the `__get__` method of the descriptor. When you assign a value like `s.shares = 75`, Python calls the `__set__` method. The descriptor can then validate the data and raise errors if necessary.

Exit the Python shell when you are done:

```python
exit()
```
