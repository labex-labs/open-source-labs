# 反转坐标轴

要反转 x 轴，我们只需使用`set_xlim`函数颠倒限制的顺序。在这个例子中，我们将 x 轴限制设置为从 5 到 0，这实际上就反转了 x 轴。

```python
ax.set_xlim(5, 0)  # decreasing time
```
