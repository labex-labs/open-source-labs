# Comprueba si dos listas tienen el mismo contenido

## Problema

Escribe una función `have_same_contents(a, b)` que tome dos listas como argumentos y devuelva `True` si tienen el mismo contenido, `False` en caso contrario. La función debe comprobar si las dos listas contienen los mismos elementos, independientemente de su orden.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `set()` en la combinación de ambas listas para encontrar los valores únicos.
2. Itera sobre ellos con un bucle `for` comparando el `count()` de cada valor único en cada lista.
3. Devuelve `False` si los conteos no coinciden para ningún elemento, `True` en caso contrario.

## Ejemplo

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
have_same_contents([1, 2, 4], [2, 4, 5]) # False
```
