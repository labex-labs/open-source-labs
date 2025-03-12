# Testing Our Implementation

Now that we have implemented our metaclass and modified the `Structure` class, it's time to test our implementation. Testing is crucial because it helps us ensure that everything is working correctly. By running tests, we can catch any potential issues early and make sure our code behaves as expected.

First, let's run the unit tests to see if our `Stock` class works as expected. Unit tests are small, isolated tests that check individual parts of our code. In this case, we want to make sure the `Stock` class functions correctly. To run the unit tests, we'll use the following command in the terminal:

```bash
python3 teststock.py
```

If everything is working correctly, all tests should pass without errors. When the tests run successfully, the output should look something like this:

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

The dots represent each test that passed, and the final `OK` indicates that all tests were successful.

Now, let's test our `Stock` class with some actual data and the table formatting functionality. This will give us a more real - world scenario to see how our `Stock` class interacts with data and how the table formatting works. We'll use the following command in the terminal:

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

In this code, we first import the necessary classes and functions. Then we read data from a CSV file into `Stock` instances. After that, we print the portfolio data and then format it into a table and print the formatted table.

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

1. We've created a mechanism to automatically collect all validator types. This means we don't have to manually keep track of all the validators, which saves us time and reduces the chance of errors.
2. We've implemented a metaclass that injects these types into the namespace of `Structure` subclasses. This allows the subclasses to use these validators without having to explicitly import them.
3. We've eliminated the need for explicit imports of validator types. This makes our code cleaner and easier to read.
4. All of this happens behind the scenes, making the code for defining new structures clean and simple.

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

Without needing to import the validator types directly, the code is more concise and easier to maintain. This is a great example of how metaclasses can improve the quality of our code.
