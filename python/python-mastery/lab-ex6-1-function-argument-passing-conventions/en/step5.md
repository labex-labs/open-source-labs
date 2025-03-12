# Rewriting the Stock Class

Now that we have a solid `Structure` base class, let's rewrite our `Stock` class to take advantage of this foundation.

## Creating the New Stock Class

Create a new file called `stock.py` with the following content:

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

Our new `Stock` class:

1. Inherits from `Structure`, eliminating the need for an `__init__` method
2. Defines `_fields` to specify the attributes
3. Provides a `cost` property to calculate the cost
4. Includes a `sell` method to reduce the number of shares

## Testing the New Stock Class

Let's create a simple test file to verify our new implementation. Create `test_stock.py`:

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

Run the test:

```bash
python3 test_stock.py
```

Expected output:

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

If you have unit tests from previous exercises, you can run them against your new implementation:

```bash
python3 teststock.py
```

Note: Some tests might fail if they're expecting specific behaviors or methods that we haven't implemented yet. That's okay! We'll continue building on this foundation in future exercises.

## Review of Our Progress

Let's review what we've accomplished:

1. Created a reusable `Structure` base class that:

   - Automatically handles attribute assignment
   - Provides a good string representation
   - Restricts attribute names to prevent errors

2. Rewrote our `Stock` class to:
   - Inherit from `Structure` for common functionality
   - Define only the fields and domain-specific methods
   - Maintain a clean, focused design

This approach makes our code:

- More maintainable (less repetition)
- More robust (better error checking)
- More readable (clearer class responsibilities)

In future exercises, we'll continue to build on this foundation to create a more sophisticated stock portfolio management system.
