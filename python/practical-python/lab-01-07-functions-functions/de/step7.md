# Übung 1.30: Ein Skript in eine Funktion umwandeln

Nehmen Sie den Code, den Sie für das `pcost.py`-Programm in Übung 1.27 geschrieben haben, und wandeln Sie ihn in eine Funktion `portfolio_cost(filename)` um. Diese Funktion nimmt einen Dateinamen als Eingabe, liest die Portfolio-Daten in dieser Datei und gibt die Gesamtkosten des Portfolios als Gleitkommazahl zurück.

Um Ihre Funktion zu verwenden, ändern Sie Ihr Programm so, dass es ungefähr so aussieht:

```python
# pcost.py
def portfolio_cost(filename):
    """
    Berechnet die Gesamtkosten (Anteile * Preis) einer Portfolio-Datei
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        zeilen = f.readlines()
        headers = zeilen[0].strip().split(",")
        for zeile in zeilen[1:]:
            zeilen_daten = zeile.strip().split(",")
            nshares = int(zeilen_daten[1])
            price = float(zeilen_daten[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Geben Sie einen Dateinamen ein:")

cost = portfolio_cost(filename)
print("Gesamtkosten:", cost)
```

Wenn Sie Ihr Programm ausführen, sollten Sie die gleiche Ausgabe wie zuvor sehen. Nachdem Sie Ihr Programm ausgeführt haben, können Sie Ihre Funktion auch interaktiv aufrufen, indem Sie Folgendes eingeben:

```bash
$ python3 -i pcost.py
```

Dies ermöglicht es Ihnen, Ihre Funktion im interaktiven Modus aufzurufen.

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

Die Möglichkeit, interaktiv mit Ihrem Code zu experimentieren, ist nützlich für das Testen und Debuggen.
