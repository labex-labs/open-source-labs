# 创建体素图

最后，我们使用 Matplotlib 中 `Axes3D` 类的 `voxels` 函数创建 3D 体素图。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
