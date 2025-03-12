# Rewriting the Stock Class

Now that we have a well - defined `Structure` base class, it's time to rewrite our `Stock` class. By using this base class, we can simplify our code and make it more organized. The `Structure` class provides a set of common functionalities that we can reuse in our `Stock` class, which is a great advantage for code maintainability and readability.

## Creating the New Stock Class

Let's start by creating a new file named `stock.py`. This file will contain our rewritten `Stock` class. Here's the code you need to put in the `stock.py` file:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        Calculate the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
```

Let's break down what this new `Stock` class does:

1. It inherits from the `Structure` class. This means that the `Stock` class can use all the features provided by the `Structure` class. One of the benefits is that we don't need to write an `__init__` method ourselves because the `Structure` class takes care of attribute assignment automatically.
2. We define `_fields` which is a tuple that specifies the attributes of the `Stock` class. These attributes are `name`, `shares`, and `price`.
3. The `cost` property is defined to calculate the total cost of the stock. It multiplies the number of `shares` by the `price`.
4. The `sell` method is used to reduce the number of shares. When you call this method with a number of shares to sell, it subtracts that number from the current number of shares.

## Testing the New Stock Class

To make sure our new `Stock` class works as expected, we need to create a test file. Let's create a file named `test_stock.py` with the following code:

```python
# test_stock.py
from stock import Stock

# Create a stock
s = Stock('GOOG', 100, 490.1)

# Check the attributes
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# Sell some shares
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# Try to set an invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # Invalid attribute (should be 'price')
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

In this test file, we first import the `Stock` class from the `stock.py` file. Then we create an instance of the `Stock` class with the name 'GOOG', 100 shares, and a price of 490.1. We print out the attributes of the stock to check if they are set correctly. After that, we sell 20 shares and print out the new number of shares and the new cost. Finally, we try to set an invalid attribute `prices` (it should be `price`). If our `Stock` class is working correctly, it should raise an `AttributeError`.

To run the test, open your terminal and enter the following command:

```bash
python3 test_stock.py
```

The expected output is as follows:

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## Running Unit Tests

If you have unit tests from previous exercises, you can run them against your new implementation. In your terminal, enter the following command:

```bash
python3 teststock.py
```

Note that some tests might fail. This could be because they expect specific behaviors or methods that we haven't implemented yet. Don't worry about it! We'll continue to build on this foundation in future exercises.

## Review of Our Progress

Let's take a moment to review what we've achieved so far:

1. We created a reusable `Structure` base class. This class:

   - Automatically handles attribute assignment, which saves us from writing a lot of repetitive code.
   - Provides a good string representation, making it easier to print and debug our objects.
   - Restricts attribute names to prevent errors, which makes our code more robust.

2. We rewrote our `Stock` class. It:
   - Inherits from the `Structure` class to reuse the common functionality.
   - Only defines the fields and domain - specific methods, which keeps the class focused and clean.
   - Has a clear and simple design, making it easy to understand and maintain.

This approach has several benefits for our code:

- It is more maintainable because we have less repetition. If we need to change something in the common functionality, we only need to change it in the `Structure` class.
- It is more robust because of the better error checking provided by the `Structure` class.
- It is more readable because the responsibilities of each class are clear.

In future exercises, we'll continue to build on this foundation to create a more sophisticated stock portfolio management system.
