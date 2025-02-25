# Diferencia simétrica basada en función

## Problema

Escribe una función `symmetric_difference_by(a, b, fn)` que tome dos listas `a` y `b`, y una función `fn`. La función debe devolver una nueva lista que contenga todos los elementos que se encuentran en cualquiera de las listas originales, pero no en ambas, después de aplicar la función proporcionada a cada elemento de ambas listas.

Para resolver este problema, puedes seguir estos pasos:

1. Crea un `set` aplicando `fn` a cada elemento de cada lista.
2. Utiliza una comprensión de lista en combinación con `fn` en cada una de ellas para conservar solo los valores no contenidos en el `set` previamente creado de la otra.
3. Concatena las dos listas obtenidas en el paso 2.

La función debe tener los siguientes parámetros:

- `a`: una lista de elementos
- `b`: una lista de elementos
- `fn`: una función que toma un elemento y devuelve un nuevo valor

La función debe devolver una nueva lista que contenga todos los elementos que se encuentran en cualquiera de las listas originales, pero no en ambas, después de aplicar la función proporcionada a cada elemento de ambas listas.

## Ejemplo

```python
from math import floor

assert symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) == [1.2, 3.4]
```
