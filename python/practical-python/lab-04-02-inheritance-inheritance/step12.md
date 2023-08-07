# Exercise 4.5: An Extensibility Problem

Suppose that you wanted to modify the `print_report()` function to support a variety of different output formats such as plain-text, HTML, CSV, or XML. To do this, you could try to write one gigantic function that did everything. However, doing so would likely lead to an unmaintainable mess. Instead, this is a perfect opportunity to use inheritance instead.

To start, focus on the steps that are involved in a creating a table. At the top of the table is a set of table headers. After that, rows of table data appear. Let's take those steps and put them into their own class. Create a file called `tableformat.py` and define the following class:

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
    raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
    raise NotImplementedError()
```

This class does nothing, but it serves as a kind of design specification for additional classes that will be defined shortly. A class like this is sometimes called an "abstract base class."

Modify the `print_report()` function so that it accepts a `TableFormatter` object as input and invokes methods on it to produce the output. For example, like this:

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

Since you added an argument to print_report(), you're going to need to modify the `portfolio_report()` function as well. Change it so that it creates a `TableFormatter` like this:

```python
# report.py

import tableformat

...
def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

Run this new code:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
... crashes ...
```

It should immediately crash with a `NotImplementedError` exception. That's not too exciting, but it's exactly what we expected. Continue to the next part.
