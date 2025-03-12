# Formatting and Printing the Portfolio Data

In this step, we're going to create a function that will help us display portfolio data in a well - organized table. A portfolio is a collection of stocks, and it's important to present this data in a clear and readable way. That's where the `print_portfolio(portfolio)` function comes in. This function will take a portfolio as input and display it in a table with headers and proper alignment.

## String Formatting in Python

In Python, there are multiple ways to format strings. String formatting is a crucial skill as it allows you to present data in a more organized and user - friendly manner.

- The `%` operator is an older style of string formatting. It's like a template where you can insert values into specific places in a string.
- The `str.format()` method is another way. It provides more flexibility and a cleaner syntax for formatting strings.
- f - strings are a feature introduced in Python 3.6 and later. They are very convenient as they allow you to embed expressions inside string literals.

For this exercise, we'll use the `%` operator. It's particularly useful when you want to create fixed - width columns, which is exactly what we need for our portfolio table.

## Implementation Instructions

1. First, open the `stock.py` file in your editor. If it's already open, that's great. This file is where we'll write our `print_portfolio` function.

2. Once the file is open, look for the `# TODO: Add print_portfolio(portfolio) function here` comment. This comment is a marker that tells us where to add our new function.

3. Below that comment, add the following function:

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

This function first prints the header row of the table, then a separator line, and finally, it loops through each stock in the portfolio and prints its details in a formatted way.

4. After adding the function, save the file. You can do this by pressing `Ctrl+S` or by selecting "File > Save" from the menu. Saving the file ensures that your changes are preserved.

5. Now, we need to test our function. Create a new file called `test_print.py`. This file will be our test script. Add the following code to it:

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

This script imports the `read_portfolio` and `print_portfolio` functions from the `stock.py` file. It then reads the portfolio data from a CSV file and uses our newly created `print_portfolio` function to display it.

6. Finally, run the test script. Open your terminal and enter the following command:

```bash
python3 test_print.py
```

If everything is working correctly, you should see output like this:

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

This output confirms that your `print_portfolio` function is working as expected. It formats and displays the portfolio data in a table with headers and aligned columns, making it easy to read.

## Understanding the String Formatting

Let's take a closer look at how the string formatting works in the `print_portfolio` function.

- `%10s` is used to format a string. The `10` indicates the width of the field, and the `s` stands for string. It aligns the string to the right within a field of width 10.
- `%10d` is for formatting an integer. The `10` is the field width, and `d` represents an integer. It also aligns the integer to the right in a field of width 10.
- `%10.2f` is used for formatting a float. The `10` is the field width, and the `.2` specifies that we want to display the float with 2 decimal places. It aligns the float to the right in a field of width 10.

This formatting ensures that all columns in our table are properly aligned, which makes the output much easier to read and understand.
