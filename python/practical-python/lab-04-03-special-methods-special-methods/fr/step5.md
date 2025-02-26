# Appel de méthode

L'appel d'une méthode est un processus en deux étapes.

1. Recherche : L'opérateur `.`
2. Appel de méthode : L'opérateur `()`

```python
>>> s = stock.Stock('GOOG',100,490.10)
>>> c = s.cost  # Recherche
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # Appel de méthode
49010.0
>>>
```
