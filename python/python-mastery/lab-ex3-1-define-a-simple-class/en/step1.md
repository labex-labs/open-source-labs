# Adding a sell Method to the Stock Class

In this step, you will add a new method called `sell(nshares)` to the `Stock` class. This method will allow you to simulate selling shares of a stock by reducing the number of shares you own.

## What is a Method?

A method is a function that is defined inside a class and operates on instances (objects) of that class. Methods have access to all the attributes of an object through the `self` parameter.

## Implementation Instructions

1. Open the `stock.py` file in the editor:

```bash
cd ~/project
```

2. Locate the `# TODO: Add sell(nshares) method here` comment in the `Stock` class.

3. Add the `sell` method that:
   - Takes a parameter `nshares` representing the number of shares to sell
   - Decreases the `shares` attribute by this amount

Here's the method you need to add:

```python
def sell(self, nshares):
    self.shares -= nshares
```

4. Save the file by pressing `Ctrl+S` or selecting "File > Save" from the menu.

5. Test your method by creating a Python script called `test_sell.py`:

```python
# test_sell.py
from stock import Stock

# Create a stock object
s = Stock('GOOG', 100, 490.10)
print(f"Initial shares: {s.shares}")

# Sell 25 shares
s.sell(25)
print(f"Shares after selling: {s.shares}")
```

6. Run the test script:

```bash
python3 test_sell.py
```

You should see output similar to this:

```
Initial shares: 100
Shares after selling: 75
```

This confirms that your `sell` method is working correctly by reducing the number of shares by the amount specified.
