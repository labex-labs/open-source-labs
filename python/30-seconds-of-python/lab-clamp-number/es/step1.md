# Clamp Number

Escribe una función `clamp_number(num, a, b)` que tome tres parámetros:

- `num` (entero o flotante): el número que se va a clampear
- `a` (entero o flotante): el límite inferior del rango
- `b` (entero o flotante): el límite superior del rango

La función debe clampear `num` dentro del rango inclusivo especificado por los valores de los límites. Si `num` está dentro del rango (`a`, `b`), devuelve `num`. De lo contrario, devuelve el número más cercano en el rango.

```python
def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))
```

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
```
