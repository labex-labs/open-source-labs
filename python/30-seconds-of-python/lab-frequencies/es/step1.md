# Frecuencias de valores

Escribe una función de Python llamada `value_frequencies(lst)` que tome una lista como argumento y devuelva un diccionario con los valores únicos de la lista como claves y sus frecuencias como valores.

Para resolver este problema, puedes seguir estos pasos:

1. Crea un diccionario vacío para almacenar las frecuencias de cada elemento único.
2. Itera a través de la lista y utiliza `collections.defaultdict` para almacenar las frecuencias de cada elemento único.
3. Utiliza `dict()` para devolver un diccionario con los elementos únicos de la lista como claves y sus frecuencias como valores.

Tu función debe devolver el diccionario con los valores únicos y sus frecuencias.

```python
from collections import defaultdict

def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
```

```python
frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
