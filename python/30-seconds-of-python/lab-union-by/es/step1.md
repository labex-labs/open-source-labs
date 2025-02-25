# Unión de listas basada en función

Escribe una función `union_by(a, b, fn)` que tome dos listas `a` y `b`, y una función `fn`. La función debe devolver una lista que contenga cada elemento que existe en cualquiera de las dos listas una vez, después de aplicar la función proporcionada a cada elemento de ambas.

Para resolver este problema, puedes seguir estos pasos:

1. Crea un `set` aplicando `fn` a cada elemento en `a`.
2. Utiliza una comprensión de lista en combinación con `fn` en `b` para conservar solo los valores no contenidos en el `set` previamente creado, `_a`.
3. Finalmente, crea un `set` a partir del resultado anterior y `a` y conviértelo en una `list`.

La función debe tener los siguientes parámetros de entrada:

- `a`: una lista de elementos
- `b`: una lista de elementos
- `fn`: una función que toma un elemento y devuelve un valor

La función debe devolver una lista de elementos.

```python
def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```
