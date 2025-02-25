# Progresión Geométrica

Escribe una función llamada `geometric_progression` que tome tres parámetros:

- `end`: un entero que representa el final del rango (inclusivo)
- `start`: un entero opcional que representa el inicio del rango (inclusivo), con un valor predeterminado de `1`
- `step`: un entero opcional que representa la razón común entre dos términos, con un valor predeterminado de `2`

La función debe devolver una lista que contiene los números en el rango especificado donde la razón entre dos términos es `step`. La lista debe comenzar con `start` y terminar con `end`.

Si `step` es igual a `1`, la función debe devolver un error.

Debes usar `range()`, `math.log()` y `math.floor()` y una comprensión de listas para crear una lista de la longitud adecuada, aplicando el paso para cada elemento.

```python
from math import floor, log

def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)]
```

```python
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```
