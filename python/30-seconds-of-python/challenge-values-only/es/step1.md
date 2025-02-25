# Valores de diccionario

## Problema

Se te da un diccionario plano, y debes crear una función que devuelva una lista plana de todos los valores en el diccionario. Tu tarea es implementar la función `values_only(flat_dict)`, que toma un diccionario plano como argumento y devuelve una lista de todos los valores en el diccionario.

Para resolver este problema, puedes usar el método `dict.values()` para devolver los valores en el diccionario dado. Luego, puedes convertir el resultado a una lista usando la función `list()`.

## Ejemplo

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```
