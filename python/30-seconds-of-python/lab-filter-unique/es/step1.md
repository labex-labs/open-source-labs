# Filtrar valores únicos de una lista

Escribe una función de Python llamada `filter_unique(lst)` que tome una lista como argumento y devuelva una nueva lista con solo los valores no únicos. Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `collections.Counter` para obtener la cuenta de cada valor en la lista.
2. Utiliza una comprensión de listas para crear una lista que contenga solo los valores no únicos.

Tu función debe satisfacer los siguientes requisitos:

- La función debe tomar una lista como argumento.
- La función debe devolver una nueva lista con solo los valores no únicos.
- La función no debe modificar la lista original.
- La función debe ser sensible a mayúsculas y minúsculas, lo que significa que 'a' y 'A' se consideran valores diferentes.

```python
def filter_unique(lst):
    # tu código aquí
```

```python
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```python
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
