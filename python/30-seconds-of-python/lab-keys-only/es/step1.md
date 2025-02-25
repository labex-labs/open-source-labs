# Claves de diccionario

Escribe una función `keys_only(flat_dict)` que tome un diccionario plano como entrada y devuelva una lista de todas sus claves.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `dict.keys()` para devolver las claves en el diccionario dado.
2. Devuelve una `list()` del resultado anterior.

```python
def keys_only(flat_dict):
  return list(flat_dict.keys())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
