# Übung 4.4: Verwenden Ihrer Klasse

Ändern Sie die `read_portfolio()`-Funktion im `report.py`-Programm so, dass sie ein Portfolio in eine Liste von `Stock`-Instanzen einliest, wie in Übung 4.3 gezeigt. Nachdem Sie das getan haben, reparieren Sie den gesamten Code in `report.py` und `pcost.py`, so dass er mit `Stock`-Instanzen statt mit Wörterbüchern funktioniert.

Hinweis: Sie sollten keine großen Änderungen am Code vornehmen müssen. Sie werden hauptsächlich die Zugriffe auf Wörterbücher wie `s['shares']` in `s.shares` umwandeln.

Sie sollten Ihre Funktionen wie zuvor ausführen können:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```
