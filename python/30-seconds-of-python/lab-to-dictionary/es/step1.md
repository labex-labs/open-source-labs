# Listas a Diccionario

Escribe una función `to_dictionary(keys, values)` que tome dos listas como entrada y devuelva un diccionario donde los elementos de la primera lista sirvan como claves y los elementos de la segunda lista sirvan como valores. La función debe utilizar `zip()` en combinación con `dict()` para combinar los valores de las dos listas en un diccionario. La función debe devolver `None` si la longitud de las dos listas no es igual.

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```
