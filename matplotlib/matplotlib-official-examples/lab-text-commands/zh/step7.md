# 向图表中添加注释

我们可以使用 `ax.annotate()` 函数向图表中添加注释。此函数接受三个参数：注释文本、要注释的点的 xy 坐标以及文本位置的 xy 坐标。我们可以使用 `arrowprops` 参数来自定义注释样式。

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
