# Übung 2.18: Tabellieren mit Zählern

Angenommen, Sie möchten die Gesamtzahl der Anteile jeder Aktie tabellieren. Dies ist mit `Counter`-Objekten einfach. Probieren Sie es aus:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Beobachten Sie genau, wie die mehreren Einträge für `MSFT` und `IBM` in `portfolio` hier zu einem einzelnen Eintrag zusammengefasst werden.

Sie können einen Zähler genauso wie ein Wörterbuch verwenden, um einzelne Werte abzurufen:

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

Wenn Sie die Werte rangieren möchten, tun Sie Folgendes:

```python
>>> # Holen Sie sich die drei am häufigsten gehaltenen Aktien
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

Lassen Sie uns ein weiteres Aktienportfolio holen und einen neuen Zähler erstellen:

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

Schließlich vereinigen wir alle Anteile mit einer einfachen Operation:

```python
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
>>>
```

Dies ist nur ein kleiner Vorgeschmack dessen, was Zähler bieten. Wenn Sie sich jedoch einmal merken, dass Sie Werte tabellieren müssen, sollten Sie einen davon in Betracht ziehen.
