# Diferencia simétrica

Escribe una función `symmetric_difference(a, b)` que tome dos listas como argumentos y devuelva su diferencia simétrica como una lista. La función no debe filtrar los valores duplicados.

Para resolver este problema, puedes seguir estos pasos:

1. Crea un conjunto a partir de cada lista.
2. Utiliza una comprensión de lista en cada una de ellas para conservar solo los valores no contenidos en el conjunto previamente creado de la otra.
3. Concatena las dos listas obtenidas en el paso 2.

```python
def symmetric_difference(a, b):
  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

```python
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
