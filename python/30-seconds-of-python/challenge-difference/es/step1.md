# Diferencia de listas

## Problema

Escribe una función de Python llamada `list_difference(a, b)` que tome dos listas como argumentos y devuelva la diferencia entre ellas. La función no debe filtrar los valores duplicados. Para resolver este problema, puedes seguir estos pasos:

1. Crea un conjunto a partir de la segunda lista `b`.
2. Utiliza una comprensión de lista en la primera lista `a` para conservar solo los valores no contenidos en el conjunto `_b` creado anteriormente.
3. Devuelve la lista resultante.

## Ejemplo

```python
list_difference([1, 2, 3], [1, 2, 4]) # [3]
```
