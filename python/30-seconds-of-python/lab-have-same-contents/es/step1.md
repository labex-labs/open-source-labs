# Comprueba si dos listas tienen el mismo contenido

Escribe una función `have_same_contents(a, b)` que tome dos listas como argumentos y devuelva `True` si tienen el mismo contenido, `False` en caso contrario. La función debe comprobar si las dos listas contienen los mismos elementos, independientemente de su orden.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `set()` en la combinación de ambas listas para encontrar los valores únicos.
2. Itera sobre ellos con un bucle `for` comparando la `count()` de cada valor único en cada lista.
3. Devuelve `False` si las cuentas no coinciden para ningún elemento, `True` en caso contrario.

```python
def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v)!= b.count(v):
      return False
  return True
```

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
```
