# Übung 2.9: Daten sammeln

In Übung 2.7 haben Sie ein Programm namens `report.py` geschrieben, das den Gewinn/Verlust eines Aktienportfolios berechnet hat. In dieser Übung werden Sie es nun so modifizieren, dass eine Tabelle wie diese erzeugt wird:

          Name     Anteile      Preis     Änderung
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

In diesem Bericht ist "Preis" der aktuelle Aktienpreis und "Änderung" die Änderung des Aktienpreises gegenüber dem ursprünglichen Kaufpreis.

Um den obigen Bericht zu generieren, müssen Sie zunächst alle in der Tabelle gezeigten Daten sammeln. Schreiben Sie eine Funktion `make_report()`, die eine Liste von Aktien und ein Wörterbuch von Preisen als Eingabe nimmt und eine Liste von Tupeln zurückgibt, die die Zeilen der obigen Tabelle enthalten.

Fügen Sie diese Funktion zur Datei `report.py` hinzu. So sollte es funktionieren, wenn Sie es interaktiv testen:

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> report = make_report(portfolio, prices)
>>> for r in report:
        print(r)

('AA', 100, 9.22, -22.980000000000004)
('IBM', 50, 106.28, 15.180000000000007)
('CAT', 150, 35.46, -47.98)
('MSFT', 200, 20.89, -30.339999999999996)
('GE', 95, 13.48, -26.889999999999997)
...
>>>
```
