# Definiendo cosas

Los nombres siempre deben estar definidos antes de ser utilizados posteriormente.

```python
def square(x):
    return x*x

a = 42
b = a + 2     # Requiere que `a` esté definido

z = square(b) # Requiere que `square` y `b` estén definidos
```

**El orden es importante.** Casi siempre se ponen las definiciones de variables y funciones cerca de la parte superior.
