# Invocação de Método

Invocar um método é um processo de duas etapas.

1.  Lookup (Pesquisa): O operador `.`
2.  Chamada de método: O operador `()`

```python
>>> s = stock.Stock('GOOG',100,490.10)
>>> c = s.cost  # Lookup
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # Method call
49010.0
>>>
```
