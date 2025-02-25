# Mapear una lista a un diccionario

## Problema

Escribe una función de Python llamada `map_dictionary(itr, fn)` que tome dos parámetros:

- `itr`: una lista de valores
- `fn`: una función que tome un valor como entrada y devuelva un valor como salida

La función debe devolver un diccionario donde los pares clave-valor consisten en el valor original como clave y el resultado de la función como valor.

Para resolver este problema, sigue estos pasos:

1. Utiliza `map()` para aplicar `fn` a cada valor de la lista.
2. Utiliza `zip()` para emparejar los valores originales con los valores producidos por `fn`.
3. Utiliza `dict()` para devolver un diccionario adecuado.

## Ejemplo

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```

En este ejemplo, la función `map_dictionary()` toma una lista `[1, 2, 3]` y una función lambda `lambda x: x * x` como entrada. La función lambda eleva al cuadrado el valor de entrada. La función devuelve un diccionario `{ 1: 1, 2: 4, 3: 9 }` donde las claves son los valores originales de la lista y los valores son los valores elevados al cuadrado.
