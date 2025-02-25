# Obtener valor anidado

Escribe una función `get(d, selectores)` que tome un diccionario o una lista `d` y una lista de selectores `selectores` como argumentos y devuelva el valor de la clave anidada indicada por la lista de selectores dada. Si la clave no existe, devuelve `None`.

Para implementar esta función, utiliza `functools.reduce()` para iterar sobre la lista `selectores`. Aplica `operator.getitem()` para cada clave en `selectores`, recuperando el valor que se usará como iterador para la siguiente iteración.

```python
from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
```

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
```
