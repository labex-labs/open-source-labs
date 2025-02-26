# Ein Funktionsaufruf durchführen

Betrachten Sie diese Funktion:

```python
def read_prices(filename, debug):
  ...
```

Sie können die Funktion mit Positionsargumenten aufrufen:

    prices = read_prices('prices.csv', True)

Oder Sie können die Funktion mit Schlüsselwortargumenten aufrufen:

```python
prices = read_prices(filename='prices.csv', debug=True)
```
