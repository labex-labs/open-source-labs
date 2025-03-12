# Creating a Base Class and Modifying the Print Function

In programming, inheritance is a powerful concept that allows us to create a hierarchy of classes. To start using inheritance for outputting data in different formats, we first need to create a base class. A base class serves as a blueprint for other classes, defining a common set of methods that its subclasses can inherit and override.

Now, let's create a base class that will define the interface for all table formatters. Open the `tableformat.py` file in the WebIDE and add the following code at the top of the file:

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

The `TableFormatter` class is an abstract base class. An abstract base class is a class that defines methods but doesn't provide implementations for them. Instead, it expects its subclasses to provide these implementations. The `NotImplementedError` exceptions are used to indicate that these methods must be overridden by subclasses. If a subclass doesn't override these methods and we try to use them, an error will be raised.

Next, we need to modify the `print_table()` function to use the `TableFormatter` class. The `print_table()` function is used to print a table of data from a list of objects. By modifying it to use the `TableFormatter` class, we can make the function more flexible and able to work with different table formats.

Replace the existing `print_table()` function with the following code:

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

The key change here is that `print_table()` now takes a `formatter` parameter, which should be an instance of `TableFormatter` or a subclass. This means that we can pass different table formatters to the `print_table()` function, and it will use the appropriate formatter to print the table. The function delegates the formatting responsibility to the formatter object by calling its `headings()` and `row()` methods.

Let's test our changes by trying to use the base `TableFormatter` class:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

When you run this code, you should see an error:

```
Traceback (most recent call last):
...
NotImplementedError
```

This error occurs because we're trying to use the abstract base class directly, but it doesn't provide implementations for its methods. Since the `headings()` and `row()` methods in the `TableFormatter` class raise `NotImplementedError`, Python doesn't know what to do when these methods are called. In the next step, we'll create a concrete subclass that does provide these implementations.
