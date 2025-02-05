# 创建第一个子图

我们将创建第一个子图，将 `rstride` 参数设置为 `10`，`cstride` 参数设置为 `0`。

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
