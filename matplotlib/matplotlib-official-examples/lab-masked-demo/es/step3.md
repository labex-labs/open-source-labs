# Eliminar puntos

Eliminaremos los puntos donde y > 0.7. Crearemos una nueva matriz x y una matriz y con solo los puntos restantes.

```python
x2 = x[y <= 0.7]
y2 = y[y <= 0.7]
```
