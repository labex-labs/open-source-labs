# Encuentra la clave de un valor en un diccionario

Escribe una función `find_key(dict, val)` que encuentre la primera clave en el diccionario proporcionado que tenga el valor dado.

Tu función debe:

- Tomar un diccionario `dict` y un valor `val` como entrada.
- Utilizar `dictionary.items()` y `next()` para devolver la primera clave que tenga un valor igual a `val`.
- Devolver la clave como salida.

```python
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
