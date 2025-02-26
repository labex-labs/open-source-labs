# Methodenaufruf

Das Aufrufen einer Methode ist ein zweistufiger Prozess.

1. Suche: Der `.`-Operator
2. Methodenaufruf: Der `()`-Operator

```python
>>> s = stock.Stock('GOOG',100,490.10)
>>> c = s.cost  # Suche
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # Methodenaufruf
49010.0
>>>
```
