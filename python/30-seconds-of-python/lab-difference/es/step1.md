# Diferencia de listas

Escribe una función de Python llamada `list_difference(a, b)` que tome dos listas como argumentos y devuelva la diferencia entre ellas. La función no debe filtrar los valores duplicados. Para resolver este problema, puedes seguir estos pasos:

1. Crea un conjunto a partir de la segunda lista `b`.
2. Utiliza una comprensión de lista en la primera lista `a` para conservar solo los valores no contenidos en el conjunto `_b` creado anteriormente.
3. Devuelve la lista resultante.

```python
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]
```

```python
difference([1, 2, 3], [1, 2, 4]) # [3]
```
