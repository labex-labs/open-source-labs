# Lokale Variablen

Variablen, die innerhalb von Funktionen zugewiesen werden, sind privat.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

In diesem Beispiel sind `filename`, `portfolio`, `line`, `fields` und `s` lokale Variablen. Diese Variablen werden nicht behalten oder zugänglich gemacht, nachdem der Funktionsaufruf beendet ist.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in?
NameError: name 'fields' is not defined
>>>
```

Lokale Variablen können auch nicht mit Variablen kollidieren, die an anderen Stellen definiert sind.
