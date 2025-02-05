# 标注坐标轴

要标注坐标轴，我们可以遍历图形的各个坐标轴，并使用 `text` 函数添加文本，同时使用 `tick_params` 函数移除刻度标签。

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
