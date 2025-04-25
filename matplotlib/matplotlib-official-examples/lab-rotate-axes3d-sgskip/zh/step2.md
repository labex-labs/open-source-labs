# 创建 3D 图

接下来，我们将使用 `plt.figure()` 和 `fig.add_subplot()` 函数创建一个 3D 图。我们还将使用 `ax.plot_wireframe()` 函数将数据集绘制成线框。

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
