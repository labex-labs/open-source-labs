# Invocación de métodos

La invocación de un método es un proceso en dos pasos.

1. Búsqueda: El operador `.`
2. Llamada de método: El operador `()`

```python
>>> s = stock.Stock('GOOG',100,490.10)
>>> c = s.cost  # Búsqueda
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # Llamada de método
49010.0
>>>
```
