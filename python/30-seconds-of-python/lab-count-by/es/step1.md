# Contar Elementos Agrupados

Escribe una función `count_by(lst, fn = lambda x: x)` que tome una lista `lst` y una función `fn` como argumentos. La función debe agrupar los elementos de la lista en función de la función dada y devolver un diccionario con la cuenta de elementos en cada grupo.

Para resolver este problema, puedes seguir estos pasos:

1. Inicializa un diccionario usando `collections.defaultdict`.
2. Utiliza `map()` para aplicar la función dada a cada elemento de la lista.
3. Itera sobre los valores mapeados e incrementa la cuenta de cada elemento en el diccionario.

La función debe devolver el diccionario resultante.

```python
from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
```

```python
from math import floor

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```
