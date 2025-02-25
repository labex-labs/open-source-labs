# Extraer valores de una lista de diccionarios

Escribe una función `pluck(lst, key)` que tome una lista de diccionarios `lst` y una clave `key` como argumentos y devuelva una lista de valores correspondientes a la `key` especificada.

Debes:

- Utilizar una comprensión de lista y `dict.get()` para obtener el valor de `key` para cada diccionario en `lst`.
- La función debe devolver una lista vacía si la lista de entrada está vacía o si la clave especificada no está presente en ninguno de los diccionarios.

```python
def pluck(lst, key):
  return [x.get(key) for x in lst]
```

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(simpsons, 'age') # [8, 36, 34, 10]
```
