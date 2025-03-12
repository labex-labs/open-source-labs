# Understanding the Descriptor Protocol

In this step, we're going to learn how descriptors work in Python by creating a simple `Stock` class. Descriptors in Python are a powerful feature that allow you to customize how attributes are accessed, set, and deleted. The descriptor protocol consists of three special methods: `__get__()`, `__set__()`, and `__delete__()`. These methods define how the descriptor behaves when an attribute is accessed, assigned a value, or deleted, respectively.

First, we need to create a new file called `stock.py` in the project directory. This file will contain our `Stock` class. Here's the code you should put in the `stock.py` file:

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

In this `Stock` class, we're using the `property` decorator to define getter and setter methods for the `name`, `shares`, and `price` attributes. These getter and setter methods act as descriptors, which means they control how these attributes are accessed and set. For example, the setter methods validate the input values to ensure they are of the correct type and within an acceptable range.

Now that we have our `stock.py` file ready, let's open a Python shell to experiment with the `Stock` class and see how descriptors work in action. To do this, open your terminal and run the following commands:

```bash
cd ~/project
python3 -i stock.py
```

The `-i` option in the `python3` command tells Python to start an interactive shell after executing the `stock.py` file. This way, we can directly interact with the `Stock` class we just defined.

In the Python shell, let's create a stock object and try accessing its attributes. Here's how you can do it:

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

When you access the `name` and `shares` attributes of the `s` object, Python is actually using the descriptor's `__get__` method behind the scenes. The `property` decorators in our class are implemented using descriptors, which means they handle the access and assignment of attributes in a controlled way.

Let's take a closer look at the class dictionary to see the descriptor objects. The class dictionary contains all the attributes and methods defined in the class. You can view the keys of the class dictionary using the following code:

```python
Stock.__dict__.keys()
```

You should see output similar to this:

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

The keys `name`, `shares`, and `price` represent the descriptor objects created by the `property` decorators.

Now, let's examine how descriptors work by manually calling their methods. We'll use the `shares` descriptor as an example. Here's how you can do it:

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

When you access an attribute like `s.shares`, Python calls the `__get__` method of the descriptor to retrieve the value. When you assign a value like `s.shares = 75`, Python calls the `__set__` method of the descriptor. The descriptor can then validate the data and raise errors if the input value is not valid.

Once you're done experimenting with the `Stock` class and descriptors, you can exit the Python shell by running the following command:

```python
exit()
```
