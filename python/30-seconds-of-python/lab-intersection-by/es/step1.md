# Intersección de listas basada en función

Escribe una función `intersection_by(a, b, fn)` que tome dos listas `a` y `b`, y una función `fn`. La función debe devolver una lista de elementos que existen en ambas listas, después de aplicar la función proporcionada a cada elemento de ambas listas.

### Entrada

- Dos listas `a` y `b` (1 <= len(a), len(b) <= 1000)
- Una función `fn` que tome un argumento y devuelva un valor

### Salida

- Una lista de elementos que existen en ambas listas, después de aplicar la función proporcionada a cada elemento de ambas listas.

```python
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```python
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
