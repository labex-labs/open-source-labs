# Comprueba si algún valor de una lista está incluido en otra lista

## Problema

Escribe una función `includes_any(lst, values)` que tome dos listas como argumentos. La función debe comprobar si algún elemento de `values` está incluido en `lst`. Si se encuentra cualquier valor, la función debe devolver `True`, de lo contrario, debe devolver `False`.

Para resolver este problema, puedes usar un bucle `for` para iterar a través de cada valor en `values`. Luego, puedes usar el operador `in` para comprobar si el valor está incluido en `lst`. Si se encuentra un valor, devuelve `True`. Si no se encuentra ningún valor, devuelve `False`.

## Ejemplo

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
