# Implementing a Concrete Formatter

Now that we have defined our abstract base class and updated the `print_table()` function, it's time to create a concrete formatter class. A concrete formatter class is one that provides actual implementations for the methods defined in the abstract base class. In our case, we'll create a class that can format data into a plain - text table.

Let's add the following class to your `tableformat.py` file. This class will inherit from the `TableFormatter` abstract base class and implement the `headings()` and `row()` methods.

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

The `TextTableFormatter` class inherits from `TableFormatter`. This means it gets all the properties and methods from the `TableFormatter` class, but it also provides its own implementations for the `headings()` and `row()` methods. These methods are responsible for formatting the table headers and rows respectively. The `headings()` method prints the headers in a nicely formatted way, followed by a line of dashes to separate the headers from the data. The `row()` method formats each row of data in a similar way.

Now, let's test our new formatter. We'll use the `stock`, `reader`, and `tableformat` modules to read data from a CSV file and print it using our new formatter.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

When you run this code, you should see the same output as before. This is because our new formatter is designed to produce the same plain - text table as the original `print_table()` function.

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

This output confirms that our `TextTableFormatter` is working correctly. The advantage of using this approach is that we've made our code more modular and extensible. By separating the formatting logic into a separate class hierarchy, we can easily add new output formats. All we need to do is create new subclasses of `TableFormatter` without modifying the `print_table()` function. This way, we can support different output formats like CSV or HTML in the future.
