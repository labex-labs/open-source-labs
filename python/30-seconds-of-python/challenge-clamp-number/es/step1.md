# Desafío de Clamp de Número

## Problema

Escribe una función `clamp_number(num, a, b)` que tome tres parámetros:

- `num` (entero o flotante): el número que se va a clampear
- `a` (entero o flotante): el límite inferior del rango
- `b` (entero o flotante): el límite superior del rango

La función debe clampear `num` dentro del rango inclusivo especificado por los valores de los límites. Si `num` está dentro del rango (`a`, `b`), devuelve `num`. De lo contrario, devuelve el número más cercano en el rango.

## Ejemplo

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
clamp_number(10, 1, 5) # 5
clamp_number(-10, -5, -1) # -5
```
