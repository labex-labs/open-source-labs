# Conjunto potencia

Escribe una función de Python llamada `powerset(iterable)` que tome un iterable como argumento y devuelva el conjunto potencia del iterable. La función debe seguir estos pasos:

1. Convertir el valor dado en una lista.
2. Usar `range()` y `itertools.combinations()` para crear un generador que devuelva todos los subconjuntos.
3. Usar `itertools.chain.from_iterable()` y `list()` para consumir el generador y devolver una lista.

```python
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
