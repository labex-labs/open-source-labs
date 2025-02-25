# Asignar valores a un diccionario

Escribe una función `map_values(obj, fn)` que tome un diccionario `obj` y una función `fn` como argumentos y devuelva un nuevo diccionario con las mismas claves que el diccionario original y valores generados al ejecutar la función proporcionada para cada valor.

```python
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```
