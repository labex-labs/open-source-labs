# Нарисуем круг на стене

Мы нарисуем круг на стене `x=0` трехмерного графика с использованием функций `Circle` и `pathpatch_2d_to_3d` Matplotlib.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
