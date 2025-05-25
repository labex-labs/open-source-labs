# Dividir lista em pedaços (chunks)

Escreva uma função `chunk(lst, size)` que recebe uma lista `lst` e um inteiro positivo `size` como argumentos e retorna uma lista de listas menores, cada uma com um tamanho máximo de `size`. Se o comprimento de `lst` não for divisível por `size`, a última lista na lista retornada deve conter os elementos restantes.

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
