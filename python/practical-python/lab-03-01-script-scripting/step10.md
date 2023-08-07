# Type Annotations

You can also add optional type hints to function definitions.

```python
def read_prices(filename: str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

The hints do nothing operationally. They are purely informational. However, they may be used by IDEs, code checkers, and other tools to do more.

In section 2, you wrote a program called `report.py` that printed out a report showing the performance of a stock portfolio. This program consisted of some functions. For example:

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

However, there were also portions of the program that just performed a series of scripted calculations. This code appeared near the end of the program. For example:

```python
...

# Output the report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

In this exercise, we're going take this program and organize it a little more strongly around the use of functions.
