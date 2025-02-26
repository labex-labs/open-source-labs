# Übung 6.2: Iteration unterstützen

Manchmal möchten Sie möglicherweise, dass eines Ihrer eigenen Objekte die Iteration unterstützt - insbesondere wenn Ihr Objekt um eine vorhandene Liste oder andere Iterable wrappt. In einer neuen Datei `portfolio.py` definieren Sie die folgende Klasse:

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

Diese Klasse soll als Schicht um eine Liste dienen, aber mit zusätzlichen Methoden wie der `total_cost`-Eigenschaft. Ändern Sie die `read_portfolio()`-Funktion in `report.py` so, dass sie eine `Portfolio`-Instanz wie folgt erstellt:

    # report.py

...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        Liest eine Datei mit einem Aktienportfolio in eine Liste von Wörterbüchern mit den Schlüsseln
        name, shares und price ein.
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)

...

Versuchen Sie, das `report.py`-Programm auszuführen. Sie werden feststellen, dass es aufgrund des Fehlers, dass `Portfolio`-Instanzen nicht iterierbar sind, spektakulär fehlschlägt.

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... abstürzt...
```

Beheben Sie dies, indem Sie die `Portfolio`-Klasse so ändern, dass sie die Iteration unterstützt:

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

Nachdem Sie diese Änderung vorgenommen haben, sollte Ihr `report.py`-Programm wieder funktionieren. Während Sie dabei sind, verbessern Sie auch Ihr `pcost.py`-Programm, um das neue `Portfolio`-Objekt zu verwenden. So:

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Berechnet die Gesamtkosten (Anteile * Preis) einer Portfolio-Datei
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

Testen Sie es, um sicherzustellen, dass es funktioniert:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
