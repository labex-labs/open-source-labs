# Mapear una lista a un diccionario

Escribe una función de Python llamada `map_dictionary(itr, fn)` que tome dos parámetros:

- `itr`: una lista de valores
- `fn`: una función que toma un valor como entrada y devuelve un valor como salida

La función debe devolver un diccionario donde los pares clave-valor consistan en el valor original como clave y el resultado de la función como valor.

Para resolver este problema, sigue estos pasos:

1. Utiliza `map()` para aplicar `fn` a cada valor de la lista.
2. Utiliza `zip()` para emparejar los valores originales con los valores producidos por `fn`.
3. Utiliza `dict()` para devolver un diccionario adecuado.

```python
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
