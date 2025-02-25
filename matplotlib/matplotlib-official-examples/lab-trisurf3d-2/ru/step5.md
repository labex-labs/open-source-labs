# Построение поверхности

Наконец, мы строим поверхность с использованием функции `plot_trisurf()`. Триангулирование в параметрическом пространстве определяет, какие точки `x`, `y`, `z` соединяются ребром.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
