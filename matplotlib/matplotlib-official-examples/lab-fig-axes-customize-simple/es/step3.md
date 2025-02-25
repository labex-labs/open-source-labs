# Agregando ejes a la figura

Agregaremos ejes a la figura utilizando el método `fig.add_axes()`. También estableceremos el color de fondo de los ejes utilizando el método `rect.set_facecolor()`.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
