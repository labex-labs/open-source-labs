# Ein Tableau drucken

Tabellieren Sie die in Schritt 2 eingelesenen Daten und verwenden Sie sie, um ein gut formatiertes Tableau zu erstellen. Beispielsweise:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Nehmen Sie diesen Code und legen Sie ihn in eine Funktion `print_portfolio()` ab, die die gleiche Ausgabe erzeugt, aber zusätzlich Tabellenüberschriften hinzufügt. Beispielsweise:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

## Hinweis:

Vervollständigen Sie die Funktion `print_portfolio()` in der Datei `stock.py`.
