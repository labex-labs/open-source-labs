# Comprueba si algún valor de una lista está incluido en otra lista

Escribe una función `includes_any(lst, values)` que tome dos listas como argumentos. La función debe comprobar si algún elemento de `values` está incluido en `lst`. Si se encuentra algún valor, la función debe devolver `True`, de lo contrario, debe devolver `False`.

Para resolver este problema, puedes usar un bucle `for` para iterar a través de cada valor en `values`. Luego, puedes usar el operador `in` para comprobar si el valor está incluido en `lst`. Si se encuentra un valor, devuelve `True`. Si no se encuentra ningún valor, devuelve `False`.

```python
def includes_any(lst, values):
  for v in values:
    if v in lst:
      return True
  return False
```

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
