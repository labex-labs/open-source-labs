# 创建箭袋图

在定义了箭头的网格和方向后，我们就可以创建箭袋图了。在本示例中，我们将使用 Matplotlib 的 `quiver` 函数来创建该图。`length` 参数设置箭头的长度，`normalize` 参数将箭头归一化为长度 1。

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
