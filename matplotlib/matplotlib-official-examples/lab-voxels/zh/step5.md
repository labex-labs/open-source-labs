# 绘制体素数组

最后，我们可以使用 `Axes3D.voxels` 函数来绘制具有指定颜色的体素数组。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
