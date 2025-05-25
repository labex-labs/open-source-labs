# Lista de Soma Parcial

Escreva uma função `partial_sum(lst)` que recebe uma lista de números como argumento e retorna uma lista de somas parciais. Sua função deve realizar as seguintes etapas:

1.  Use `itertools.accumulate()` para criar a soma acumulada para cada elemento na lista.
2.  Use `list()` para converter o resultado em uma lista.
3.  Retorne a lista de somas parciais.

```python
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```python
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```
