# Creating Additional Formatters

In programming, inheritance is a powerful concept that allows us to create new classes based on existing ones. This helps in reusing code and making our programs more extensible. In this part of the experiment, we'll use inheritance to create two new formatters for different output formats: CSV and HTML. These formatters will inherit from a base class, which means they'll share some common behavior while having their own unique ways of formatting data.

Now, let's add the following classes to your `tableformat.py` file. These classes will define how to format data in CSV and HTML formats respectively.

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

The `CSVTableFormatter` class is designed to format data in the CSV (Comma-Separated Values) format. The `headings` method takes a list of headers and prints them separated by commas. The `row` method takes a list of data for a single row and also prints them separated by commas.

The `HTMLTableFormatter` class, on the other hand, is used to generate HTML table code. The `headings` method creates the table headers using HTML `<th>` tags, and the `row` method creates a table row using HTML `<td>` tags.

Let's test these new formatters to see how they work.

1. First, let's test the CSV formatter:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

In this code, we first import the necessary modules. Then we read data from a CSV file named `portfolio.csv` and create instances of the `Stock` class. Next, we create an instance of the `CSVTableFormatter` class. Finally, we use the `print_table` function to print the portfolio data in CSV format.

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

Here, we create an instance of the `HTMLTableFormatter` class and use the `print_table` function again to print the portfolio data in HTML format.

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

As you can see, each formatter produces output in a different format, but they all share the same interface defined by the `TableFormatter` base class. This is a great example of the power of inheritance and polymorphism. We can write code that works with the base class, and it will automatically work with any subclass.

The `print_table()` function doesn't need to know anything about the specific formatter being used. It just calls the methods defined in the base class, and the appropriate implementation is selected based on the type of formatter provided. This makes our code more flexible and easier to maintain.
