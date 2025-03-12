# Adding Type Checking to print_table()

In this step, we're going to make the `print_table()` function in the `tableformat.py` file better. We'll add a check to see if the `formatter` parameter is a valid `TableFormatter` instance. Why do we need this? Well, type checking is like a safety net for your code. It helps make sure that the data you're working with is of the right type, which can prevent a lot of hard - to - find bugs.

## Understanding Type Checking in Python

Type checking is a really useful technique in programming. It allows you to catch errors early in the development process. In Python, we often deal with different types of objects, and sometimes we expect a certain type of object to be passed to a function. To check if an object is of a specific type or a subclass of it, we can use the `isinstance()` function. For example, if you have a function that expects a list, you can use `isinstance()` to make sure the input is indeed a list.

## Modifying the print_table() Function

First, open the `tableformat.py` file in your code editor. Scroll down to the bottom of the file, and you'll find the `print_table()` function. Here's what it looks like initially:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

This function takes in some data, a list of columns, and a formatter. It then uses the formatter to print a table. But right now, it doesn't check if the formatter is of the right type.

Let's modify it to add the type check. We'll use the `isinstance()` function to check if the `formatter` parameter is an instance of `TableFormatter`. If it's not, we'll raise a `TypeError` with a clear message. Here's the modified code:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## Testing Your Type Checking Implementation

Now that we've added the type check, we need to make sure it works. Let's create a new Python file called `test_tableformat.py`. Here's the code you should put in it:

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

In this code, we first read some portfolio data. Then we define a new formatter class called `MyFormatter` that doesn't inherit from `TableFormatter`. We try to use this non - compliant formatter in the `print_table()` function. If our type check is working, it should raise a `TypeError`.

To run the test, open your terminal and navigate to the directory where the `test_tableformat.py` file is located. Then run the following command:

```bash
python test_tableformat.py
```

If everything is working correctly, you should see an output like this:

```
Test passed - caught error: Expected a TableFormatter
```

This output confirms that our type checking is working as expected. Now, the `print_table()` function will only accept a formatter that is an instance of `TableFormatter` or one of its subclasses.
