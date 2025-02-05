# 向网格布局规范（GridSpec）中添加子图

我们可以使用 `fig.add_subplot()` 函数向网格布局规范（GridSpec）中添加子图。我们可以使用网格布局规范（GridSpec）对象的索引表示法来指定子图在网格中的位置。例如，`gs[0, :]` 指定第一行和所有列。

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
