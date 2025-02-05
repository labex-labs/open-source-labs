# 向第二个内部网格布局添加子图

现在我们要向第二个内部网格布局添加子图。我们将创建三个子图：`ax4`、`ax5` 和 `ax6`。

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
