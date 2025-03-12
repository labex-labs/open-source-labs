# Creating Additional Formatters

Now let's implement two additional formatters for different output formats: CSV and HTML. These will demonstrate the power of inheritance for creating extensible code.

Add the following classes to your `tableformat.py` file:

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

Let's test these new formatters:

1. First, let's test the CSV formatter:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

You should see the following CSV-formatted output:

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. Now let's test the HTML formatter:

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

You should see the following HTML-formatted output:

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

As you can see, each formatter produces output in a different format, but they all share the same interface defined by the `TableFormatter` base class. This demonstrates the power of inheritance and polymorphism - we can write code that works with the base class, and it will automatically work with any subclass.

The `print_table()` function doesn't need to know anything about the specific formatter being used - it just calls the methods defined in the base class, and the appropriate implementation is selected based on the type of formatter provided.
