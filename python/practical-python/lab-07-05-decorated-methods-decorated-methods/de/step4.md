# Übung 7.11: Praxis der Klassenmethoden

In Ihren Dateien `report.py` und `portfolio.py` ist die Erstellung eines `Portfolio` -Objekts etwas verwirrt. Beispielsweise hat das `report.py` -Programm Code wie diesen:

```python
def read_portfolio(filename, **opts):
    '''
    Liest eine Datei mit einem Aktienportfolio in eine Liste von Wörterbüchern mit den Schlüsseln
    name, shares und price ein.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

und die `portfolio.py` -Datei definiert `Portfolio()` mit einem eigenartigen Initialisierer wie diesem:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
  ...
```

Ehrlich gesagt ist die Verantwortungsabfolge ein bisschen verwirrend, weil der Code verteilt ist. Wenn eine `Portfolio` -Klasse eine Liste von `Stock` -Instanzen enthalten soll, sollten Sie vielleicht die Klasse etwas klarer gestalten. So:

```python
# portfolio.py

import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)
  ...
```

Wenn Sie ein Portfolio aus einer CSV -Datei lesen möchten, sollten Sie vielleicht eine Klassenmethode dafür erstellen:

```python
# portfolio.py

import fileparse
import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

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

Um diese neue Portfolio -Klasse zu verwenden, können Sie jetzt Code wie diesen schreiben:

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

Machen Sie diese Änderungen an der `Portfolio` -Klasse und ändern Sie den `report.py` -Code, um die Klassenmethode zu verwenden.
