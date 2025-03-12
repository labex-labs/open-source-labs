# Applying Validators to a Stock Class

In this step, we'll apply our validators to a real-world example. We'll create a `Stock` class that uses our validators to ensure the values of its attributes are valid.

## Creating the Stock Class

Create a new file called `stock.py` in the WebIDE. Add the following code:

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

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
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

In this class:

1. We import the `PositiveInteger` and `PositiveFloat` validators from our `validate` module
2. We define a `Stock` class with properties for `name`, `shares`, and `price`
3. We use property setters to validate that `shares` is a positive integer and `price` is a positive float
4. We provide a `cost` method that calculates the total cost of the stock

## Testing the Stock Class

Let's test our `Stock` class to see if the validators work. Open a new terminal and start the Python interpreter:

```bash
python3
```

Now import and test our `Stock` class:

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

You should see output similar to:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

This shows that our validators are working as expected. The `Stock` class rejects attempts to set invalid values for `shares` and `price`.

## Understanding How Inheritance Helps

The beauty of using our validators is that we can easily compose different validation rules together. If we want to add more validation rules, we can create new validator classes and compose them using multiple inheritance.

For example, if we wanted to ensure that the stock name is not empty, we could:

1. Import `NonEmptyString` from `validate`
2. Add a property setter for `name` that uses `NonEmptyString.check()`

This demonstrates how inheritance, particularly multiple inheritance with the `super()` function, allows us to build flexible, reusable components that can be combined in different ways.

You can exit the Python interpreter when you're done:

```python
exit()
```
