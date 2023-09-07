# Exercise 2.11: Adding some headers

Suppose you had a tuple of header names like this:

```python
headers = ('Name', 'Shares', 'Price', 'Change')
```

Add code to your program that takes the above tuple of headers and creates a string where each header name is right-aligned in a 10-character wide field and each field is separated by a single space.

```python
'      Name     Shares      Price      Change'
```

Write code that takes the headers and creates the separator string between the headers and data to follow. This string is just a bunch of "-" characters under each field name. For example:

```python
'---------- ---------- ---------- -----------'
```

When you're done, your program should produce the table shown at the top of this exercise.

          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

Here's a solution:

```python
import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.DictReader(f)
        for row in rows:
            holding = {
                'name': row['name'],
                'shares': int(row['shares']),
                'price': float(row['price'])
            }
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                stock_name = row[0]
                stock_price = float(row[1])
                prices[stock_name] = stock_price

    return prices

def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        stock_name = stock['name']
        shares = stock['shares']
        price = prices.get(stock_name)
        if price is not None:
            change = price - stock['price']
            row = (stock_name, shares, price, change)
            report.append(row)

    return report

def create_header_string(headers):
    header_string = ''
    for header in headers:
        header_string += f'{header:>10s} '

    return header_string.strip()

def create_separator_string(headers):
    separator_string = ''
    for header in headers:
        separator_string += f'{("-" * 10):>10s} '

    return separator_string.strip()

portfolio = read_portfolio('/home/labex/project/portfolio.csv')
prices = read_prices('/home/labex/project/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
header_string = create_header_string(headers)
separator_string = create_separator_string(headers)

print(header_string)
print(separator_string)

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
```