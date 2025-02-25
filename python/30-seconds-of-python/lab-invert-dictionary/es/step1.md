# Invertir un diccionario

Escribe una función de Python llamada `invert_dictionary(obj)` que tome un diccionario `obj` como argumento y devuelva un nuevo diccionario con las claves y los valores invertidos. El diccionario de entrada `obj` tendrá valores hashables únicos. El diccionario de salida debe tener las mismas claves que el diccionario de entrada, pero los valores deben ser las claves del diccionario de entrada.

Debes usar `dictionary.items()` en combinación con una comprensión de lista para crear el nuevo diccionario.

```python
def invert_dictionary(obj):
  return { value: key for key, value in obj.items() }
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```
