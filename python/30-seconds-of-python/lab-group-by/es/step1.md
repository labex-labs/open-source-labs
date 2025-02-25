# Agrupar elementos de una lista

Escribe una función `group_by(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos y devuelva un diccionario donde las claves son los resultados de aplicar `fn` a los elementos de `lst` y los valores son listas de elementos de `lst` que producen la clave correspondiente cuando `fn` se aplica a ellos.

Por ejemplo, si tenemos una lista de números `[6.1, 4.2, 6.3]` y queremos agruparlos por su parte entera, podemos usar la función `floor` del módulo `math` como función de agrupamiento. La salida esperada sería `{4: [4.2], 6: [6.1, 6.3]}`.

```python
from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
