# Creating a User-Friendly API for Mixins

While mixins are powerful, they require users to understand multiple inheritance, which can be complex. In this step, we'll create a more user-friendly API by enhancing the `create_formatter()` function.

Open the `tableformat.py` file again:

```bash
cd ~/project
code tableformat.py
```

Find the `create_formatter()` function, which currently looks like this:

```python
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Now, let's modify this function to support optional arguments for our mixins. Replace the function with this enhanced version:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting
    upper_headers : bool, optional
        Whether to convert headers to uppercase
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Apply mixins if requested
    if column_formats and upper_headers:
        class CustomFormatter(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif column_formats:
        class CustomFormatter(ColumnFormatMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif upper_headers:
        class CustomFormatter(UpperHeadersMixin, formatter_cls):
            pass
        return CustomFormatter()
    else:
        return formatter_cls()
```

This enhanced function dynamically creates a custom formatter class with the requested mixins based on the provided arguments.

Let's test our enhanced function with different combinations of options:

First, let's try with column formatting:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

You should see formatted columns:

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

Now, let's try with uppercase headers:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

You should see uppercase headers:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Finally, let's combine both options:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

This should display both formatted columns and uppercase headers:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

It also works with other formatter types:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

This should produce CSV output with formatted columns:

```
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
```

By enhancing the `create_formatter()` function, we've created a user-friendly API that hides the complexity of multiple inheritance while still providing the flexibility of mixins.
