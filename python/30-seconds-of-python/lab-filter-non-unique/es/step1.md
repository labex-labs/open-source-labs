# Filtrar valores no únicos de una lista

Escribe una función de Python llamada `filter_non_unique(lst)` que tome una lista como argumento y devuelva una nueva lista con solo los valores únicos. Para resolver este problema, puedes seguir estos pasos:

1. Utiliza el método `collections.Counter` para obtener la cuenta de cada valor en la lista.
2. Utiliza una comprensión de lista para crear una lista que contenga solo los valores únicos.

```python
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]
```

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```
