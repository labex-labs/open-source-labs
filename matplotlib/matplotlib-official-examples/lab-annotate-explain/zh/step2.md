# 用箭头连接两个点

在这一步中，我们将用箭头连接这两个点。我们将使用 `annotate` 函数来创建箭头，并自定义箭头的样式和颜色。

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
