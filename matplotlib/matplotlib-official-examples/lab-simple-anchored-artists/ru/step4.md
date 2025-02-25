# Нарисуйте круг

Нарисуйте круг в координатах оси.

```python
ada = AnchoredDrawingArea(20, 20, 0, 0,
                          loc='upper right', pad=0., frameon=False)
p = Circle((10, 10), 10)
ada.da.add_artist(p)
ax.add_artist(ada)
```
