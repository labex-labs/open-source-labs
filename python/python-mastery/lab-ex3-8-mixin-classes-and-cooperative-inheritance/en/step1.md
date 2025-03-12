# Understanding the Problem with Column Formatting

In this step, we're going to look into a limitation in our current table formatting implementation. We'll also examine some possible solutions to this problem.

First, let's understand what we're going to do. We'll open the VSCode editor and look at the `tableformat.py` file in the project directory. This file is important because it contains the code that allows us to format tabular data in different ways, like in text, CSV, or HTML formats.

To open the file, we'll use the following commands in the terminal. The `cd` command changes the directory to the project directory, and the `code` command opens the `tableformat.py` file in VSCode.

```bash
cd ~/project
code tableformat.py
```

When you open the file, you'll notice that there are several classes defined. These classes play different roles in formatting the table data.

- `TableFormatter`: This is an abstract base class. It has methods that are used for formatting the table headings and rows. Think of it as a blueprint for other formatter classes.
- `TextTableFormatter`: This class is used to output the table in plain text format.
- `CSVTableFormatter`: It's responsible for formatting the table data in CSV (Comma-Separated Values) format.
- `HTMLTableFormatter`: This class formats the table data in HTML format.

There's also a `print_table()` function in the file. This function uses the formatter classes we just mentioned to display the tabular data.

Now, let's see how these classes work by running some Python code. Open a terminal and start a Python session. The following code imports the necessary functions and classes from the `tableformat.py` file, creates a `TextTableFormatter` object, and then uses the `print_table()` function to display the portfolio data.

```python
python3 -c "
from tableformat import print_table, TextTableFormatter, portfolio
formatter = TextTableFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

After running the code, you should see output similar to this:

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

One way to fix this is to modify the `print_table()` function to accept format specifications. The following code shows how we can do this. We define a new `print_table()` function that takes an additional `formats` parameter. Inside the function, we use these format specifications to format each value in the row.

```python
python3 -c "
from tableformat import TextTableFormatter, portfolio

def print_table(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [(fmt % getattr(r, fieldname))
             for fieldname, fmt in zip(fields, formats)]
        formatter.row(rowdata)

formatter = TextTableFormatter()
print_table(portfolio,
            ['name','shares','price'],
            ['%s','%d','%0.2f'],
            formatter)
"
```

This solution works, but it has a drawback. Changing the function's interface might break existing code that uses the old version of the `print_table()` function.

Another approach is to create a custom formatter by subclassing. We can create a new class that inherits from `TextTableFormatter` and override the `row()` method to apply the desired formatting.

```python
python3 -c "
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        formats = ['%s','%d','%0.2f']
        rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
        super().row(rowdata)

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

This solution also works, but it's not very convenient. Every time we want different formatting, we have to create a new class. And we're limited to the specific formatter type we're subclassing from, in this case, `TextTableFormatter`.

In the next step, we'll explore a more elegant solution using mixin classes.
