# Vorbereitungen

Um loszulegen, betrachten wir zunächst einige Grundlagen mit einem etwas einfachereren Datensatz - einem Portfolio von Aktienpositionen. Erstellen Sie eine Datei `readport.py` und legen Sie diesen Code darin ab:

```python
# readport.py

import csv

# Eine Funktion, die eine Datei in eine Liste von Dictionaries einliest
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

Diese Datei liest einige einfache Aktienmarkt-Daten in der Datei `portfolio.csv` ein. Verwenden Sie die Funktion, um die Datei zu lesen und die Ergebnisse anzuschauen:

Öffnen Sie eine Python-Shell und versuchen Sie Folgendes:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
 {'name': 'IBM', 'price': 91.1,'shares': 50},
 {'name': 'CAT', 'price': 83.44,'shares': 150},
 {'name': 'MSFT', 'price': 51.23,'shares': 200},
 {'name': 'GE', 'price': 40.37,'shares': 95},
 {'name': 'MSFT', 'price': 65.1,'shares': 50},
 {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```

In diesen Daten besteht jede Zeile aus einem Aktiennamen, einer Anzahl gehaltenen Anteile und einem Kaufpreis. Es gibt mehrere Einträge für bestimmte Aktiennamen wie MSFT und IBM.
