# 自定义子图

我们可以根据需要自定义子图。例如，我们可以使用 `fig.suptitle()` 函数设置图形的标题，还可以使用 `format_axes()` 函数格式化坐标轴。

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
