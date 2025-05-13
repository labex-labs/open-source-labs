# Understanding the Problem with Column Formatting

In this step, we're going to look into a limitation in our current table formatting implementation. We'll also examine some possible solutions to this problem.

First, let's understand what we're going to do. We'll open the VSCode editor and look at the `tableformat.py` file in the project directory. This file is important because it contains the code that allows us to format tabular data in different ways, like in text, CSV, or HTML formats.

To open the file, we'll use the following commands in the terminal. The `cd` command changes the directory to the project directory, and the `code` command opens the `tableformat.py` file in VSCode.

```bash
cd ~/project
touch tableformat.py
```

When you open the file, you'll notice that there are several classes defined. These classes play different roles in formatting the table data.

- `TableFormatter`: This is an abstract base class. It has methods that are used for formatting the table headings and rows. Think of it as a blueprint for other formatter classes.
- `TextTableFormatter`: This class is used to output the table in plain text format.
- `CSVTableFormatter`: It's responsible for formatting the table data in CSV (Comma-Separated Values) format.
- `HTMLTableFormatter`: This class formats the table data in HTML format.

There's also a `print_table()` function in the file. This function uses the formatter classes we just mentioned to display the tabular data.

Now, let's see how these classes work. In your `/home/labex/project` directory, create a new file named `step1_test1.py` using your editor or the `touch` command. Add the following Python code to it:

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Save the file and run it from your terminal:

```bash
python3 step1_test1.py
```

After running the script, you should see output similar to this:

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

Now, let's find the problem. Notice that the values in the `price` column aren't formatted consistently. Some values have one decimal place, like 32.2, while others have two decimal places, like 51.23. In financial data, we usually want the formatting to be consistent.

Here's what we want the output to look like:

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

One way to fix this is to modify the `print_table()` function to accept format specifications. Let's see how this works _without_ actually modifying `tableformat.py`. Create a new file named `step1_test2.py` with the following content. This script redefines the `print_table` function locally for demonstration purposes.

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

Run this script:

```bash
python3 step1_test2.py
```

This approach demonstrates passing formats, but modifying `print_table` has a drawback: changing the function's interface might break existing code that uses the original version.

Another approach is to create a custom formatter by subclassing. We can create a new class that inherits from `TextTableFormatter` and override the `row()` method. Create a file `step1_test3.py`:

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Run the script:

```bash
python3 step1_test3.py
```

This solution works for demonstrating subclassing, but creating a new class for every formatting variation isn't convenient. Plus, you're tied to the base class you inherit from (here, `TextTableFormatter`).

In the next step, we'll explore a more elegant solution using mixin classes.
