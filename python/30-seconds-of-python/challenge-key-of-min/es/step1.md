# Clave del valor mínimo

## Problema

Escribe una función `key_of_min(d)` que tome un diccionario `d` como argumento y devuelva la clave del valor mínimo en el diccionario.

Para resolver este problema, puedes usar la función integrada `min()` con el parámetro `key` establecido en `dict.get()`. Esto devolverá la clave del valor mínimo en el diccionario.

## Ejemplo

```python
key_of_min({'a':4, 'b':0, 'c':13}) # 'b'
```

En este ejemplo, el diccionario `{'a':4, 'b':0, 'c':13}` se pasa como argumento a la función `key_of_min()`. La función devuelve la clave `'b'`, que corresponde al valor mínimo en el diccionario.
