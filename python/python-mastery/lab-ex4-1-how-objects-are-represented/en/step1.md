# Creating a Simple Stock Class

In this step, we will create a simple class to represent a stock. This will serve as our foundation for exploring how Python objects work internally.

Open a Python interactive shell by typing the following command in the terminal:

```bash
python3
```

Once the Python prompt (`>>>`) appears, define a `SimpleStock` class with the following attributes and methods:

```python
>>> class SimpleStock:
...     def __init__(self, name, shares, price):
...         self.name = name
...         self.shares = shares
...         self.price = price
...     def cost(self):
...         return self.shares * self.price
...
```

After defining the class, create two instances to represent different stocks:

```python
>>> goog = SimpleStock('GOOG', 100, 490.10)
>>> ibm = SimpleStock('IBM', 50, 91.23)
```

These instances represent 100 shares of Google stock at $490.10 per share and 50 shares of IBM stock at $91.23 per share.

Let's verify that our instances are working properly by checking their attributes and calculating their cost:

```python
>>> goog.name
'GOOG'
>>> goog.shares
100
>>> goog.price
490.1
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
```

The `cost()` method multiplies the number of shares by the price per share to calculate the total cost of holding those shares.
