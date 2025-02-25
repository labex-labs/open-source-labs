# Übung 1.33: Einlesen von der Befehlszeile

Im `pcost.py`-Programm ist der Name der Eingabedatei im Code hartcodiert:

```python
# pcost.py

def portfolio_cost(filename):
 ...
    # Ihr Code hier
 ...

cost = portfolio_cost('portfolio.csv')
print('Gesamtkosten:', cost)
```

Das ist für das Lernen und Testen in Ordnung, aber in einem echten Programm würden Sie das vermutlich nicht tun.

Stattdessen könnten Sie den Dateinamen als Argument an ein Skript übergeben. Versuchen Sie, den unteren Teil des Programms wie folgt zu ändern:

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Berechnet die Gesamtkosten (Anteile * Preis) einer Portfolio-Datei
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        zeilen = csv.reader(f)
        headers = next(zeilen)  # Überspringe die Kopfzeile
        for zeile in zeilen:
            if len(zeile) < 3:
                print("Überspringe ungültige Zeile:", zeile)
                continue
            try:
                nshares = int(zeile[1])
                price = float(zeile[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Überspringe ungültige Zeile:", zeile)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Gesamtkosten:', cost)
```

`sys.argv` ist eine Liste, die die übergebenen Argumente auf der Befehlszeile enthält (sofern vorhanden).

Um Ihr Programm auszuführen, müssen Sie Python aus der Kommandozeile ausführen.

Beispielsweise aus bash auf Unix:

```bash
$ python3 pcost.py portfolio.csv
Gesamtkosten: 44671.15
bash %
```
