# Exercise 4.6: Using Inheritance to Produce Different Output

The `TableFormatter` class you defined in part (a) is meant to be
extended via inheritance. In fact, that's the whole idea. To
illustrate, define a class `TextTableFormatter` like this:

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

Modify the `portfolio_report()` function like this and try it:

```python
# report.py
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
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
```

This should produce the same output as before:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

However, let's change the output to something else. Define a new
class `CSVTableFormatter` that produces output in CSV format:

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

Modify your main program as follows:

```python
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
    formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)
```

You should now see CSV output like this:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
```

Using a similar idea, define a class `HTMLTableFormatter`
that produces a table with the following output:

```
<tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
<tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
<tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
<tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
<tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
<tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
<tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
<tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>
```

Test your code by modifying the main program to create a
`HTMLTableFormatter` object instead of a
`CSVTableFormatter` object.
