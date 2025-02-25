# Построение триангуляции Делоне

Мы построим триангуляцию с использованием функции triplot.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw=1)
ax1.set_title('Triplot of Delaunay Triangulation')
```
