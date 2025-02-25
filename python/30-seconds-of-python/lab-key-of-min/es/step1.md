# Clave del valor mínimo

Escribe una función `key_of_min(d)` que tome como argumento un diccionario `d` y devuelva la clave del valor mínimo en el diccionario.

Para resolver este problema, puedes usar la función integrada `min()` con el parámetro `key` establecido en `dict.get()`. Esto devolverá la clave del valor mínimo en el diccionario.

```python
def key_of_min(d):
  return min(d, key = d.get)
```

```python
key_of_min({'a':4, 'b':0, 'c':13}) # b
```
