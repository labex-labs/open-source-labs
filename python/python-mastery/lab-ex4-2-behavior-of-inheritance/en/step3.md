# Applying Validators to a Stock Class

In this step, we're going to see how our validators work in a real - world situation. Validators are like little checkers that make sure the data we use meets certain rules. We'll create a `Stock` class. A class is like a blueprint for creating objects. In this case, the `Stock` class will represent a stock in the stock market, and we'll use our validators to make sure the values of its attributes (like the number of shares and the price) are valid.

## Creating the Stock Class

First, we need to create a new file. In the WebIDE, create a new file called `stock.py`. This file will hold the code for our `Stock` class. Now, add the following code to the `stock.py` file:

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

Let's break down what this code does:

1. We start by importing the `PositiveInteger` and `PositiveFloat` validators from our `validate` module. These validators will help us make sure that the number of shares is a positive integer and the price is a positive float.
2. Then we define a `Stock` class. Inside the class, we have an `__init__` method. This method is called when we create a new `Stock` object. It takes in three parameters: `name`, `shares`, and `price`, and assigns them to the object's attributes.
3. We use properties and setters to validate the values of `shares` and `price`. A property is a way to control access to an attribute, and a setter is a method that gets called when we try to set the value of that attribute. When we set the `shares` attribute, the `PositiveInteger.check` method is called to make sure the value is a positive integer. Similarly, when we set the `price` attribute, the `PositiveFloat.check` method is called to make sure the value is a positive float.
4. Finally, we have a `cost` method. This method calculates the total cost of the stock by multiplying the number of shares by the price.

## Testing the Stock Class

Now that we've created our `Stock` class, we need to test it to see if the validators are working correctly. Open a new terminal and start the Python interpreter. You can do this by running the following command:

```bash
python3
```

Once the Python interpreter is running, we can import and test our `Stock` class. Enter the following code into the Python interpreter:

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

When you run this code, you should see output similar to the following:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

This output shows that our validators are working as expected. The `Stock` class doesn't allow us to set invalid values for `shares` and `price`. When we try to set an invalid value, an error is raised, and we can catch and print that error.

## Understanding How Inheritance Helps

One of the great things about using our validators is that we can easily combine different validation rules. Inheritance is a powerful concept in Python that allows us to create new classes based on existing ones. With multiple inheritance, we can use the `super()` function to call methods from multiple parent classes.

For example, if we want to make sure that the stock name is not empty, we can follow these steps:

1. Import the `NonEmptyString` validator from the `validate` module. This validator will help us check if the stock name is not an empty string.
2. Add a property setter for the `name` attribute in the `Stock` class. This setter will use the `NonEmptyString.check()` method to validate the stock name.

This shows how inheritance, especially multiple inheritance with the `super()` function, lets us build components that are flexible and can be reused in different combinations.

When you're done testing, you can exit the Python interpreter by running the following command:

```python
exit()
```
