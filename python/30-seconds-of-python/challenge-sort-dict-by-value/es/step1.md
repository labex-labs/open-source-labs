# Desafío de ordenar un diccionario

## Problema

Escribe una función llamada `sort_dict_by_value(d, reverse=False)` que tome un diccionario `d` y lo ordene por sus valores. La función debe devolver un nuevo diccionario con las mismas claves que el diccionario original, pero con los valores ordenados en orden ascendente. Si el parámetro `reverse` se establece en `True`, la función debe ordenar el diccionario en orden descendente.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `dict.items()` para obtener una lista de pares de tuplas a partir de `d`.
2. Ordena la lista utilizando una función lambda y `sorted()`.
3. Utiliza `dict()` para convertir la lista ordenada de nuevo en un diccionario.
4. Utiliza el parámetro `reverse` en `sorted()` para ordenar el diccionario en orden inverso, basado en el segundo argumento.

**⚠️ ATENCIÓN:** Los valores del diccionario deben ser del mismo tipo.

## Ejemplo

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True) # {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
