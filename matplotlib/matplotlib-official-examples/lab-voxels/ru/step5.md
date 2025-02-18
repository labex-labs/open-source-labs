# Построение воксельного массива

Наконец, мы можем использовать функцию `Axes3D.voxels` для построения воксельного массива с заданными цветами.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
