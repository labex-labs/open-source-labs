# 绘制曲面

最后，我们使用 `plot_trisurf()` 函数绘制曲面。参数空间中的三角形决定了哪些 `x`、`y`、`z` 点由一条边连接。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
