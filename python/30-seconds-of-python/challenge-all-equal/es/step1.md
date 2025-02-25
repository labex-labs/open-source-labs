# Comprueba si los elementos de una lista son idénticos

## Problema

Escribe una función `all_equal(lst)` que tome una lista como argumento y devuelva `True` si todos los elementos de la lista son idénticos, y `False` en caso contrario.

Para resolver este problema, puedes utilizar los siguientes pasos:

1. Utiliza `set()` para eliminar los elementos duplicados de la lista.
2. Utiliza `len()` para comprobar si la longitud del conjunto es `1`.
3. Si la longitud del conjunto es `1`, devuelve `True`. En caso contrario, devuelve `False`.

## Ejemplo

```python
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```
