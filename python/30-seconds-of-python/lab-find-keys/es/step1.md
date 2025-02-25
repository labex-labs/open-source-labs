# Encontrar claves con un valor dado

Escribe una función de Python llamada `find_keys(dictionary, value)` que tome un diccionario y un valor como argumentos y devuelva una lista de todas las claves en el diccionario que tienen el valor dado. Si no hay claves con el valor dado, la función debe devolver una lista vacía.

Para resolver este problema, puedes usar el método `dictionary.items()`, que devuelve un generador que produce pares clave-valor del diccionario. Luego, puedes usar una comprensión de lista para filtrar las claves que tienen el valor dado.

```python
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```
