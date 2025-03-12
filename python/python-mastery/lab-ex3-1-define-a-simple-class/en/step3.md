# Formatting and Printing the Portfolio Data

In this step, you will create a function called `print_portfolio(portfolio)` that displays the portfolio data in a nicely formatted table with headers and proper alignment.

## String Formatting in Python

Python offers several ways to format strings:

- The `%` operator (older style)
- The `str.format()` method
- f-strings (Python 3.6+)

In this exercise, we'll use the `%` operator for string formatting, which is especially useful for creating fixed-width columns.

## Implementation Instructions

1. Open the `stock.py` file in the editor if it's not already open.

2. Locate the `# TODO: Add print_portfolio(portfolio) function here` comment.

3. Add the following function below the comment:

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

4. Save the file by pressing `Ctrl+S` or selecting "File > Save" from the menu.

5. Create a test script called `test_print.py` to verify your function:

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

6. Run the test script:

```bash
python3 test_print.py
```

You should see output like this:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

This confirms that your `print_portfolio` function is correctly formatting and displaying the portfolio data in a table with headers and aligned columns.

## Understanding the String Formatting

In the `print_portfolio` function:

- `%10s` formats a string right-aligned in a field of width 10
- `%10d` formats an integer right-aligned in a field of width 10
- `%10.2f` formats a float right-aligned in a field of width 10 with 2 decimal places

This formatting ensures that all columns are properly aligned, making the output easier to read.
