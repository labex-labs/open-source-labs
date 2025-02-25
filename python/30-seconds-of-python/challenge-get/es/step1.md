# Obtener valor anidado

## Problema

Escribe una función `get(d, selectores)` que tome un diccionario o una lista `d` y una lista de selectores `selectores` como argumentos y devuelva el valor de la clave anidada indicada por la lista de selectores dada. Si la clave no existe, devuelve `None`.

Para implementar esta función, utiliza `functools.reduce()` para iterar sobre la lista `selectores`. Aplica `operator.getitem()` para cada clave en `selectores`, recuperando el valor que se usará como iterador para la siguiente iteración.

## Ejemplo

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
get(users, ['freddy', 'age']) # None
```
