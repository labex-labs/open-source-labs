# Creating a User-Friendly API for Mixins

Mixins are a powerful feature in Python, but they can be a bit tricky for beginners because they involve multiple inheritance, which can get quite complex. In this step, we're going to make things easier for users by improving the `create_formatter()` function. This way, users won't have to worry too much about the details of multiple inheritance.

First, you need to open the `tableformat.py` file. You can do this by running the following commands in your terminal. The `cd` command changes the directory to your project folder, and the `code` command opens the `tableformat.py` file in your code editor.

```bash
cd ~/project
code tableformat.py
```

Once the file is open, find the `create_formatter()` function. Currently, it looks like this:

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

This function takes a name as an argument and returns the corresponding formatter. But we want to make it more flexible. We're going to modify it so that it can accept optional arguments for our mixins.

Replace the existing `create_formatter()` function with the enhanced version below. This new function allows you to specify column formats and whether to convert headers to uppercase.

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

This enhanced function works by first determining the base formatter class based on the `name` argument. Then, depending on whether `column_formats` and `upper_headers` are provided, it creates a custom formatter class that includes the appropriate mixins. Finally, it returns an instance of the custom formatter class.

Now, let's test our enhanced function with different combinations of options.

First, let's try using column formatting. Run the following command in your terminal. This command imports the necessary functions and data from the `tableformat.py` file, creates a formatter with column formatting, and then prints a table using that formatter.

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

You should see the table with formatted columns. The output will look like this:

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

Next, let's try using uppercase headers. Run the following command:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

You should see the table with uppercase headers. The output will be:

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

Finally, let's combine both options. Run this command:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

This should display a table with both formatted columns and uppercase headers. The output will be:

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

The enhanced function also works with other formatter types. For example, let's try it with the CSV formatter. Run the following command:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

This should produce CSV output with formatted columns. The output will be:

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

By enhancing the `create_formatter()` function, we've created a user-friendly API. Users can now easily use mixins without having to understand the complex details of multiple inheritance. This gives them the flexibility to customize the formatters according to their needs.
