# Definiendo funciones

Es una buena idea poner todo el código relacionado con una sola _tarea_ en un solo lugar. Utiliza una función.

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Una función también simplifica las operaciones repetidas.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```
