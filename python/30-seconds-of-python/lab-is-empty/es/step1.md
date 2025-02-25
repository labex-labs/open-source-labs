# Colección está vacía

Escribe una función de Python llamada `is_empty(val)` que tome un valor como parámetro y devuelva `True` si el valor es una secuencia o colección vacía, y `False` en caso contrario.

Para comprobar si una secuencia o colección está vacía, puedes usar el operador `not` para probar el valor de verdad de la secuencia o colección proporcionada. Si la secuencia o colección está vacía, el operador `not` devolverá `True`.

Tu función debe ser capaz de manejar los siguientes tipos de secuencias y colecciones:

- Listas
- Tuplas
- Conjuntos
- Diccionarios
- Cadenas
- Rangos

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```
