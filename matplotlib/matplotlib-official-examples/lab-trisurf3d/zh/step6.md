# 创建三维曲面

我们将使用 `plot_trisurf` 函数创建三维曲面：

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```
