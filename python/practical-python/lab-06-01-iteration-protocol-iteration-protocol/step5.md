# Exercise 6.2: Supporting Iteration

On occasion, you might want to make one of your own objects support iteration--especially if your object wraps around an existing list or other iterable. In a new file `portfolio.py`, define the following class:

```python
# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

This class is meant to be a layer around a list, but with some extra methods such as the `total_cost` property. Modify the `read_portfolio()` function in `report.py` so that it creates a `Portfolio` instance like this:

    # report.py
    ...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        Read a stock portfolio file into a list of dictionaries with keys
        name, shares, and price.
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)
    ...

Try running the `report.py` program. You will find that it fails spectacularly due to the fact that `Portfolio` instances aren't iterable.

```python
>>> import report
>>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
... crashes ...
```

Fix this by modifying the `Portfolio` class to support iteration:

```python
class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

After you've made this change, your `report.py` program should work again. While you're at it, fix up your `pcost.py` program to use the new `Portfolio` object. Like this:

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

Test it to make sure it works:

```python
>>> import pcost
>>> pcost.portfolio_cost('Data/portfolio.csv')
44671.15
>>>
```
