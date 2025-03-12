# Testing Our Implementation

Now that we have implemented our metaclass and modified the `Structure` class, let's test our implementation to make sure everything is working correctly.

First, let's run the unit tests to see if our `Stock` class works as expected:

```bash
python3 teststock.py
```

If everything is working correctly, all tests should pass without errors. The output should look something like:

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Now, let's test our `Stock` class with some actual data and the table formatting functionality:

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Read portfolio data into Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Format and print the portfolio data
print('\nFormatted table:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

You should see output similar to this:

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Take a moment to appreciate what we've accomplished:

1. We've created a mechanism to automatically collect all validator types
2. We've implemented a metaclass that injects these types into the namespace of `Structure` subclasses
3. We've eliminated the need for explicit imports of validator types
4. All of this happens behind the scenes, making the code for defining new structures clean and simple

The final `stock.py` file is remarkably clean compared to what it would have been without our metaclass:

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Without needing to import the validator types directly, the code is more concise and easier to maintain.
