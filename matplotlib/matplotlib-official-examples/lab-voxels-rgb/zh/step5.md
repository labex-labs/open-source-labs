# 绘制体素图

最后，我们可以使用 `ax.voxels` 函数来绘制体素图。我们将传入 RGB 值、球体的条件、面颜色、边颜色和线宽。

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
