# Creating a Table Formatter Using Attribute Access

In programming, attribute access is a fundamental concept that allows us to interact with the properties of objects. Now, we're going to put what we've learned about attribute access into practice. We'll create a useful utility: a table formatter. This formatter will take a collection of objects and display them in a tabular format, making the data easier to read and understand.

## Creating the tableformat.py Module

First, we need to create a new Python file. This file will hold the code for our table formatter.

To create the file, follow these steps:

1. In the WebIDE, click on the "File" menu.
2. From the dropdown, select "New File".
3. Save the newly created file as `tableformat.py` in the `/home/labex/project/` directory.

Now that we have our file, let's write the code for the `print_table()` function inside `tableformat.py`. This function will be responsible for formatting and printing our objects in a table.

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

Let's break down what this function does:

1. It takes two arguments: a sequence of objects and a list of attribute names. The sequence of objects is the data we want to display, and the list of attribute names tells the function which properties of the objects to show.
2. It prints a header row. The header row contains the names of the attributes we're interested in.
3. It prints a separator line. This line helps to visually separate the header from the data.
4. For each object in the sequence, it prints the value of each specified attribute. It uses the `getattr()` function to access the attribute value of each object.

Now, let's test our `print_table()` function to see if it works as expected.

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

When you run the above code, you should see the following output:

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

One of the great things about our `print_table()` function is its flexibility. We can change the columns that are displayed just by changing the `fields` list.

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

Running this code will give you the following output:

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

The power of this approach lies in its generality. We can use the same `print_table()` function to print tables for any type of object, as long as we know the names of the attributes we want to display. This makes our table formatter a very useful tool in our programming toolkit.
