# Extraer valores de una lista de diccionarios

## Problema

Escribe una función `pluck(lst, key)` que tome una lista de diccionarios `lst` y una clave `key` como argumentos y devuelva una lista de valores correspondientes a la clave `key` especificada.

Debes:

- Utilizar una comprensión de lista y `dict.get()` para obtener el valor de `key` para cada diccionario en `lst`.
- La función debe devolver una lista vacía si la lista de entrada está vacía o si la clave especificada no está presente en ninguno de los diccionarios.

## Ejemplo

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
print(pluck(simpsons, 'age')) # [8, 36, 34, 10]
```
