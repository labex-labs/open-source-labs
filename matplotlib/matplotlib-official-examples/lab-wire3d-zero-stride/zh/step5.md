# 创建第二个子图

我们将创建第二个子图，将 `rstride` 参数设置为 `0`，`cstride` 参数设置为 `10`。

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
