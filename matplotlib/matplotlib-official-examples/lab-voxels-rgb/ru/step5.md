# Построение воксельной диаграммы

Наконец, мы можем построить воксельную диаграмму с использованием функции `ax.voxels`. Мы передадим RGB-значения, условие для сферы, цвета граней, цвета рёбер и толщину линии.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
