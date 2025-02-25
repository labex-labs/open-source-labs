# Asignar valores a un diccionario

## Problema

Escribe una función `map_values(obj, fn)` que tome un diccionario `obj` y una función `fn` como argumentos y devuelva un nuevo diccionario con las mismas claves que el diccionario original y valores generados al ejecutar la función proporcionada para cada valor.

## Ejemplo

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```

## Limitaciones

- La función debe funcionar para cualquier diccionario y función que cumplan con los requisitos.
- La función no debe modificar el diccionario original.
