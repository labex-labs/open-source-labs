# Übung 2.4: Eine Liste von Tupeln

Die Datei `portfolio.csv` enthält eine Liste von Aktien in einem Portfolio. In Übung 1.30 haben Sie eine Funktion `portfolio_cost(filename)` geschrieben, die diese Datei ausliest und eine einfache Berechnung durchführt.

Ihr Code hätte ungefähr so aussehen müssen:

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Berechnet die Gesamtkosten (Anteile * Preis) einer Portfolio-Datei'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

Nutzen Sie diesen Code als groben Leitfaden und erstellen Sie eine neue Datei `report.py`. In dieser Datei definieren Sie eine Funktion `read_portfolio(filename)`, die eine gegebene Portfolio-Datei öffnet und sie in eine Liste von Tupeln einliest. Dazu werden Sie den obigen Code leicht modifizieren.

Zunächst werden Sie statt `total_cost = 0` eine Variable definieren, die zunächst als leere Liste initialisiert wird. Beispielsweise:

```python
portfolio = []
```

Als nächstes werden Sie statt die Kosten zu summieren jede Zeile in ein Tupel umwandeln, genauso wie Sie es im letzten Übungsaufgabe getan haben, und es dieser Liste hinzufügen. Beispielsweise:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Schließlich werden Sie die resultierende `portfolio`-Liste zurückgeben.

Experimentieren Sie interaktiv mit Ihrer Funktion (ein kleiner Hinweis: Um dies zu tun, müssen Sie zunächst das `report.py`-Programm im Interpreter ausführen):

_Hinweis: Verwenden Sie `-i`, wenn Sie die Datei im Terminal ausführen_

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

Diese Liste von Tupeln, die Sie erstellt haben, ist sehr ähnlich einem 2D-Array. Beispielsweise können Sie auf eine bestimmte Spalte und Zeile über einen Zugriff wie `portfolio[row][column]` zugreifen, wobei `row` und `column` ganze Zahlen sind.

Allerdings können Sie auch die letzte for-Schleife mit einer Anweisung wie dieser umschreiben:

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
