# 绘制数据

使用`plot_wireframe`在三个子图中的每个子图上绘制数据。

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
