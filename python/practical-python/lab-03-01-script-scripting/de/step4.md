# Funktionen definieren

Es ist eine gute Idee, den gesamten Code, der mit einer einzelnen _Aufgabe_ zusammenhängt, an einem Ort zu sammeln. Verwenden Sie eine Funktion.

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Eine Funktion vereinfacht auch wiederholte Vorgänge.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```
