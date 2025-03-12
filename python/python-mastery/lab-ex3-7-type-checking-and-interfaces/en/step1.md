# Adding Type Checking to print_table()

In this step, you will enhance the `print_table()` function in `tableformat.py` to check if the formatter parameter is a valid `TableFormatter` instance. This improves type safety in your code.

## Understanding Type Checking in Python

Type checking helps catch errors early by verifying that function parameters are of the expected types. In Python, we can use `isinstance()` to check if an object is an instance of a specific class or its subclass.

## Modifying the print_table() Function

Open the `tableformat.py` file in the editor and locate the `print_table()` function at the bottom:

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

Modify this function to check if the `formatter` parameter is an instance of `TableFormatter`. If not, raise a `TypeError` with an appropriate message:

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

Let's verify that your type checking works. Create a new Python file called `test_tableformat.py` with the following code:

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

Run the test file:

```bash
python test_tableformat.py
```

You should see an output like:

```
Test passed - caught error: Expected a TableFormatter
```

This confirms that your type checking is working correctly. The code now enforces that the formatter must be an instance of `TableFormatter` (or one of its subclasses).
