# Создать воксельную диаграмму

Наконец, мы создаем трехмерную воксельную диаграмму с использованием функции `voxels` класса `Axes3D` в Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
