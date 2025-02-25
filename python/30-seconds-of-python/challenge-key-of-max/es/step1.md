# Clave del valor máximo

## Problema

Escribe una función `key_of_max(d)` que tome un diccionario `d` como argumento y devuelva la clave del valor máximo en el diccionario. Si hay múltiples claves con el mismo valor máximo, devuelve cualquiera de ellas.

Para resolver este problema, puedes usar la función `max()` con el parámetro `key` establecido en `dict.get()`. Esto devolverá la clave del valor máximo en el diccionario.

## Ejemplo

```python
key_of_max({'a':4, 'b':0, 'c':13}) # 'c'
```
