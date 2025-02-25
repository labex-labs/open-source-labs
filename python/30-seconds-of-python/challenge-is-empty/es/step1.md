# La colección está vacía

## Problema

Escribe una función de Python llamada `is_empty(val)` que tome un valor como parámetro y devuelva `True` si el valor es una secuencia o colección vacía, y `False` en caso contrario.

Para comprobar si una secuencia o colección está vacía, puedes usar el operador `not` para probar el valor de verdad de la secuencia o colección proporcionada. Si la secuencia o colección está vacía, el operador `not` devolverá `True`.

Tu función debe ser capaz de manejar los siguientes tipos de secuencias y colecciones:

- Listas
- Tuplas
- Conjuntos
- Diccionarios
- Cadenas de texto
- Rangos

## Ejemplo

```python
assert is_empty([]) == True
assert is_empty({}) == True
assert is_empty('') == True
assert is_empty(set()) == True
assert is_empty(range(0)) == True
assert is_empty([1, 2]) == False
assert is_empty({'a': 1, 'b': 2}) == False
assert is_empty('text') == False
assert is_empty(set([1, 2])) == False
assert is_empty(range(2)) == False
```
