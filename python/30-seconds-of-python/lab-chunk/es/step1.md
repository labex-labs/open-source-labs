# Dividir una lista en trozos

Escribe una función `chunk(lst, size)` que tome una lista `lst` y un entero positivo `size` como argumentos y devuelva una lista de listas más pequeñas, cada una de las cuales tiene un tamaño máximo de `size`. Si la longitud de `lst` no es divisible uniformemente por `size`, la última lista en la lista devuelta debe contener los elementos restantes.

```python
from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
```

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
```
