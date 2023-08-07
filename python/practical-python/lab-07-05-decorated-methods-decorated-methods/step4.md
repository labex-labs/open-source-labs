# Exercise 7.11: Class Methods in Practice

In your `report.py` and `portfolio.py` files, the creation of a `Portfolio` object is a bit muddled. For example, the `report.py` program has code like this:

```python
def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

and the `portfolio.py` file defines `Portfolio()` with an odd initializer like this:

```python
class Portfolio:
    def __init__(self, holdings):
        self.holdings = holdings
    ...
```

Frankly, the chain of responsibility is all a bit confusing because the code is scattered. If a `Portfolio` class is supposed to contain a list of `Stock` instances, maybe you should change the class to be a bit more clear. Like this:

```python
# portfolio.py

import stock

class Portfolio:
    def __init__(self):
        self.holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)
    ...
```

If you want to read a portfolio from a CSV file, maybe you should make a class method for it:

```python
# portfolio.py

import fileparse
import stock

class Portfolio:
    def __init__(self):
        self.holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self
```

To use this new Portfolio class, you can now write code like this:

```python
>>> from portfolio import Portfolio
>>> with open('Data/portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

Make these changes to the `Portfolio` class and modify the `report.py` code to use the class method.
