# Manejo del caso del diccionario vacío

Nuestra función actual tiene un problema: se romperá si el diccionario de entrada `d` está vacío. Arreglemos eso. Modifica `key_of_max.py` para que se vea así:

```python
def key_of_max(d):
  """
  Devuelve la clave asociada con el valor máximo en el diccionario 'd'.

  Si múltiples claves comparten el valor máximo, cualquiera de ellas puede ser devuelta.
  """
  if not d:  # Check if the dictionary is empty
      return None
  return max(d, key=d.get)
```

Las líneas agregadas hacen lo siguiente:

- **`if not d:`**: En Python, un diccionario vacío se considera "falso" (falsy). Esta declaración `if` verifica si el diccionario `d` está vacío.
- **`return None`**: Si el diccionario está vacío, no hay un valor máximo, así que devolvemos `None`. Esta es una forma estándar de indicar la ausencia de un valor en Python. Esto evita que la función `max()` lance un error.

Este es un paso crucial al escribir código robusto: ¡siempre considera los casos extremos (edge cases)!
