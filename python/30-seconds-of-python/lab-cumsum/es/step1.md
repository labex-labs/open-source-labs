# Lista de sumas parciales

Escribe una función `partial_sum(lst)` que tome una lista de números como argumento y devuelva una lista de sumas parciales. Tu función debe realizar los siguientes pasos:

1. Utiliza `itertools.accumulate()` para crear la suma acumulada para cada elemento de la lista.
2. Utiliza `list()` para convertir el resultado en una lista.
3. Devuelve la lista de sumas parciales.

```python
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```python
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```
