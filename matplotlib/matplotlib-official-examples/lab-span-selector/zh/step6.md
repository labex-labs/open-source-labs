# 创建一个跨度选择器

我们将使用 `matplotlib.widgets.SpanSelector` 创建一个跨度选择器对象。

```python
span = SpanSelector(
    ax1,
    onselect,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:blue"),
    interactive=True,
    drag_from_anywhere=True
)
```
