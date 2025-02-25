# Создание многоугольника программно

Для создания многоугольника программно нам нужно создать объект `Figure` и объект `Axes`. Затем мы можем создать объект `PolygonSelector` и добавить вершины в него. Наконец, мы можем нарисовать многоугольник на `Axes`.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Add three vertices
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
