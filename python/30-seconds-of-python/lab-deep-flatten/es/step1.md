# Aplanar lista anidada

Escribe una función `deep_flatten(lst)` que tome una lista `lst` como argumento y devuelva una nueva lista que sea la versión profundamente aplanada de `lst`. La función debe utilizar recursión y la función `isinstance()` con `collections.abc.Iterable` para comprobar si un elemento es iterable. Si un elemento es iterable, la función debe aplicar `deep_flatten()` recursivamente a ese elemento. En caso contrario, la función debe devolver una lista que contenga solo ese elemento.

```python
from collections.abc import Iterable

def deep_flatten(lst):
  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
```

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
```
