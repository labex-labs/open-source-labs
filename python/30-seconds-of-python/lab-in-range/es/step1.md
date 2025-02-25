# Número en el rango

Escribe una función `in_range(n, start, end = 0)` que tome tres parámetros:

- `n`: un número para comprobar si se encuentra dentro del rango
- `start`: el inicio del rango
- `end`: el final del rango (opcional, valor predeterminado es 0)

La función debe devolver `True` si el número dado `n` se encuentra dentro del rango especificado, y `False` en caso contrario. Si el parámetro `end` no se especifica, el rango se considera que va de `0` a `start`.

```python
def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start
```

```python
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```
