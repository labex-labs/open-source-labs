# Implementing a Concrete Formatter

Now that we have our abstract base class and updated `print_table()` function, let's create a concrete formatter class that implements the required methods. Add the following class to your `tableformat.py` file:

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain-text table.
    """
    def headings(self, headers):
        """
        Generate plain-text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain-text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

The `TextTableFormatter` class inherits from `TableFormatter` and provides concrete implementations for the `headings()` and `row()` methods. These implementations format the data as a plain-text table, similar to what the original `print_table()` function did.

Let's test our new formatter:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

You should see the same output as before:

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

This confirms that our `TextTableFormatter` is working correctly. The output is the same as with the original function, but now we can create other formatters for different output formats.

By separating the formatting logic into a separate class hierarchy, we've made our code more modular and extensible. We can now add new output formats by creating new subclasses of `TableFormatter` without modifying the `print_table()` function.
