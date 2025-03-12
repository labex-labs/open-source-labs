# Understanding the Problem with Column Formatting

In this step, we'll explore a limitation in our current table formatting implementation and examine potential solutions.

First, let's open the VSCode editor and take a look at the `tableformat.py` file in the project directory. This file contains the code for formatting tabular data in different ways (text, CSV, HTML).

```bash
cd ~/project
code tableformat.py
```

When you open the file, you'll see several classes defined:

- `TableFormatter`: An abstract base class with methods for formatting table headings and rows
- `TextTableFormatter`: For plain text table output
- `CSVTableFormatter`: For CSV format output
- `HTMLTableFormatter`: For HTML format output

Additionally, there's a `print_table()` function that uses these formatters to display tabular data.

Let's explore how these classes work by running some Python code. Open a terminal and start a Python session:

```python
python3 -c "
from tableformat import print_table, TextTableFormatter, portfolio
formatter = TextTableFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

You should see output similar to this:

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

Now, let's identify the problem: notice how the `price` column values aren't consistently formatted. Some have one decimal place (32.2), others have two (51.23). For financial data, we typically want consistent formatting.

Here's what we want:

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

We could modify the `print_table()` function to accept format specifications:

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

This works, but it changes the function's interface, which might break existing code.

Another approach would be to create a custom formatter by subclassing:

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

This also works, but it's cumbersome. We have to create a new class each time we want different formatting, and we're tied to a specific formatter type (TextTableFormatter in this case).

In the next step, we'll explore a more elegant solution using mixin classes.
