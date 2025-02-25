# Unión de listas basada en función

## Problema

Escribe una función `union_by(a, b, fn)` que tome dos listas `a` y `b`, y una función `fn`. La función debe devolver una lista que contenga cada elemento que existe en cualquiera de las dos listas una vez, después de aplicar la función proporcionada a cada elemento de ambas.

Para resolver este problema, puedes seguir estos pasos:

1. Crea un `set` aplicando `fn` a cada elemento en `a`.
2. Utiliza una comprensión de listas en combinación con `fn` en `b` para conservar solo los valores no contenidos en el `set` previamente creado, `_a`.
3. Finalmente, crea un `set` a partir del resultado anterior y `a` y conviértelo en una `list`.

La función debe tener los siguientes parámetros de entrada:

- `a`: una lista de elementos
- `b`: una lista de elementos
- `fn`: una función que toma un elemento y devuelve un valor

La función debe devolver una lista de elementos.

## Ejemplo

Aquí hay un ejemplo de lo que debe hacer `union_by()`:

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```

En este ejemplo, `union_by()` toma dos listas `[2.1]` y `[1.2, 2.3]`, y una función `floor()`. La función aplica `floor()` a cada elemento de ambas listas, creando un `set` de `{2}`. Luego, utiliza una comprensión de listas para conservar solo los valores no contenidos en el `set`, que es `[1.2]`. Finalmente, crea un `set` a partir del resultado anterior y `[2.1]`, que es `{1.2, 2.1}`, y lo convierte en una lista `[1.2, 2.1]`.
