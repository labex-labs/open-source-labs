# Combinar valores de diccionarios

Escribe una función `combine_values(*dicts)` que tome dos o más diccionarios como argumentos y devuelva un nuevo diccionario que combine los valores de los diccionarios de entrada. La función debe realizar los siguientes pasos:

1. Crea un nuevo `collections.defaultdict` con `list` como el valor predeterminado para cada clave.
2. Itera sobre los diccionarios de entrada y, para cada diccionario:
   - Itera sobre las claves del diccionario.
   - Agrega el valor de la clave a la lista de valores para esa clave en el `defaultdict`.
3. Convierte el `defaultdict` a un diccionario regular utilizando la función `dict()`.
4. Devuelve el diccionario resultante.

La función debe tener la siguiente firma:

```python
def combine_values(*dicts):
    pass
```

```python
from collections import defaultdict

def combine_values(*dicts):
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)
```

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```
