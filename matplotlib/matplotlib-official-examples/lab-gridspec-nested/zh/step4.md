# 向内部网格布局添加子图

现在我们将向内部网格布局添加子图。我们将创建三个子图：`ax1`、`ax2` 和 `ax3`。

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
