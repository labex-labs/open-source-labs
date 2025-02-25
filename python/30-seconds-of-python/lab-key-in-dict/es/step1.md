# Comprueba si una clave existe en un diccionario

Escribe una función `key_in_dict(d, key)` que tome un diccionario `d` y una clave `key` como argumentos y devuelva `True` si la clave existe en el diccionario, `False` en caso contrario.

```python
def key_in_dict(d, key):
  return (key in d)
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
