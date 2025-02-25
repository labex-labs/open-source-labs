# Comprueba si una lista incluye todos los valores

## Problema

Escribe una función llamada `includes_all(lst, values)` que tome dos listas como parámetros. La función debe comprobar si todos los valores de la lista `values` están incluidos en la lista `lst`. Si todos los valores están incluidos, la función debe devolver `True`. Si cualquiera de los valores no está incluido, la función debe devolver `False`.

Para resolver este problema, debes:

1. Utilizar un bucle `for` para iterar a través de cada valor de la lista `values`.
2. Comprobar si el valor actual está incluido en la lista `lst` utilizando el operador `in`.
3. Si el valor no está incluido, devolver `False`.
4. Si todos los valores están incluidos, devolver `True`.

## Ejemplo

```python
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```
