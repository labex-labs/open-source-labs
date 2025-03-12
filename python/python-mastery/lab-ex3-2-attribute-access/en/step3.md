# Creating a Table Formatter Using Attribute Access

Now let's apply what we've learned about attribute access to create a useful utility: a table formatter that can display a collection of objects in a tabular format.

## Creating the tableformat.py Module

First, let's create a new file called `tableformat.py` in the project directory:

1. In the WebIDE, click on "File" menu, then select "New File"
2. Save the file as `tableformat.py` in the `/home/labex/project/` directory

Now, let's implement the `print_table()` function in `tableformat.py`:

```python
def print_table(objects, fields):
    """
    Print a collection of objects as a formatted table.

    Args:
        objects: A sequence of objects
        fields: A list of attribute names
    """
    # Print the header
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Print the separator line
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Print the data
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

This function:

1. Takes a sequence of objects and a list of attribute names
2. Prints a header row with the attribute names
3. Prints a separator line
4. For each object, prints the value of each specified attribute

Let's test our function:

```python
# Open a Python interactive shell
python3

# Import our modules
from stock import read_portfolio
import tableformat

# Read the portfolio data
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a table with name, shares, and price columns
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Output:

```
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

We can change the columns displayed just by changing the fields list:

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

Output:

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

The power of this approach is that we can use the same function to print tables for any type of object, as long as we know the attribute names.
