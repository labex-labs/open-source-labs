# Varios valores de retorno

Las funciones solo pueden devolver un valor. Sin embargo, una función puede devolver varios valores devolviéndolos en una tupla.

```python
def divide(a,b):
    q = a // b      # Cociente
    r = a % b       # Resto
    return q, r     # Devuelve una tupla
```

Ejemplo de uso:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
