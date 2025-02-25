# Combinar diccionarios

Escribe una función `merge_dictionaries(*dicts)` que tome dos o más diccionarios como argumentos y devuelva un nuevo diccionario que contenga todos los pares clave-valor de los diccionarios de entrada.

Tu función debe crear un nuevo diccionario y recorrer los diccionarios de entrada, utilizando `dictionary.update()` para agregar los pares clave-valor de cada uno al resultado.

```python
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
