# Построить края

Постройте края с использованием метода `plot`. Мы построим три линии вдоль координат X и Y, и одну линию вдоль координат X и Z.

```python
# Plot edges
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
