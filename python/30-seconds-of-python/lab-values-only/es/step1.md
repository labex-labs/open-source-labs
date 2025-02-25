# Valores de diccionario

Se te da un diccionario plano y debes crear una función que devuelva una lista plana de todos los valores del diccionario. Tu tarea es implementar la función `values_only(flat_dict)`, que toma un diccionario plano como argumento y devuelve una lista de todos los valores del diccionario.

Para resolver este problema, puedes utilizar el método `dict.values()` para devolver los valores del diccionario dado. Luego, puedes convertir el resultado a una lista utilizando la función `list()`.

```python
def values_only(flat_dict):
  return list(flat_dict.values())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```
