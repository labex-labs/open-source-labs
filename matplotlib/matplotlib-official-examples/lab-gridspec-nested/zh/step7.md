# 设置坐标轴格式

我们将使用 `format_axes` 函数来设置所有子图的坐标轴格式。这个函数会为每个子图添加一个文本标签，并移除刻度标签。

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
