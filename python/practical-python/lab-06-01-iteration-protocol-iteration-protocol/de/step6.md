# Übung 6.3: Ein passenderer Container erstellen

Wenn Sie eine Containerklasse erstellen, möchten Sie oft mehr tun als nur Iteration. Ändern Sie die `Portfolio`-Klasse so, dass sie einige andere spezielle Methoden hat, wie folgt:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

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

Jetzt machen Sie einige Experimente mit dieser neuen Klasse:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> len(portfolio)
7
>>> portfolio[0]
Stock('AA', 100, 32.2)
>>> portfolio[1]
Stock('IBM', 50, 91.1)
>>> portfolio[0:3]
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44)]
>>> 'IBM' in portfolio
True
>>> 'AAPL' in portfolio
False
>>>
```

Eine wichtige Beobachtung dazu - allgemein wird Code als "pythonisch" angesehen, wenn er das übliche Vokabular der Art, wie andere Teile von Python normalerweise funktionieren, spricht. Für Containerobjekte ist das Unterstützen von Iteration, Indexierung, Enthaltensein und anderen Arten von Operatoren ein wichtiger Teil hiervon.
