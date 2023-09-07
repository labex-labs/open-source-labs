# Exercise 2.12: Formatting Challenge

How would you modify your code so that the price includes the currency symbol (\$) and the output looks like this:

          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100      $9.22     -22.98
           IBM         50    $106.28      15.18
           CAT        150     $35.46     -47.98
          MSFT        200     $20.89     -30.34
            GE         95     $13.48     -26.89
          MSFT         50     $20.89     -44.21
           IBM        100    $106.28      35.84

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

def format_price(price):
    return f'${price:.2f}'

portfolio = read_portfolio('/home/labex/project/portfolio.csv')
prices = read_prices('/home/labex/project/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
header_string = create_header_string(headers)
separator_string = create_separator_string(headers)

print(header_string)
print(separator_string)

for name, shares, price, change in report:
    formatted_price = format_price(price)
    print(f'{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}')
```