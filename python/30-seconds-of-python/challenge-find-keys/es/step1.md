# Encontrar claves con un valor dado

## Problema

Escribe una función de Python llamada `find_keys(dictionary, value)` que tome un diccionario y un valor como argumentos y devuelva una lista de todas las claves en el diccionario que tienen el valor dado. Si no hay claves con el valor dado, la función debe devolver una lista vacía.

Para resolver este problema, puedes utilizar el método `dictionary.items()`, que devuelve un generador que produce pares clave-valor del diccionario. Luego, puedes utilizar una comprensión de lista para filtrar las claves que tienen el valor dado.

## Ejemplo

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```

En este ejemplo, la función `find_keys()` se llama con un diccionario `ages` y un valor `10`. La función devuelve una lista de claves que tienen el valor `10`, que son `'Peter'` y `'Anna'`.
