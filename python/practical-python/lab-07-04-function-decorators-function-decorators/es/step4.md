# Decoradores

Poner envoltorios alrededor de funciones es extremadamente común en Python. Tan común que hay una sintaxis especial para ello.

```python
def add(x, y):
    return x + y
add = logged(add)

# Sintaxis especial
@logged
def add(x, y):
    return x + y
```

La sintaxis especial realiza exactamente los mismos pasos que se muestran arriba. Un decorador es solo una nueva sintaxis. Se dice que _decora_ la función.
