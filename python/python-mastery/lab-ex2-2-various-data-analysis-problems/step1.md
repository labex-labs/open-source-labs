# Preliminaries

To get started, let's review some basics with a slightly simpler dataset--
a portfolio of stock holdings. Create a file `readport.py` and put this
code in it:

```python
# readport.py

import csv

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

This file reads some simple stock market data in the file `portfolio.csv`. Use
the function to read the file and look at the results:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
>>>
```

In this data, each row consists of a stock name, a number of held
shares, and a purchase price. There are multiple entries for
certain stock names such as MSFT and IBM.
