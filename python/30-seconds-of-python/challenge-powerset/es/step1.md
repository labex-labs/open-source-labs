# Desafío del conjunto potencia

## Problema

Escribe una función de Python llamada `powerset(iterable)` que tome un iterable como argumento y devuelva el conjunto potencia del iterable. La función debe seguir estos pasos:

1. Convertir el valor dado en una lista.
2. Utilizar `range()` y `itertools.combinations()` para crear un generador que devuelva todos los subconjuntos.
3. Utilizar `itertools.chain.from_iterable()` y `list()` para consumir el generador y devolver una lista.

## Ejemplo

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
