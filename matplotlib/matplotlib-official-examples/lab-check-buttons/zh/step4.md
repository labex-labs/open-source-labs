# 添加复选按钮

现在，我们将使用 `CheckButtons` 函数为图表添加复选按钮。我们将把绘制的线条作为标签传递，并设置每条线的初始可见性。我们还将调整复选按钮的属性，使其与绘制线条的颜色相匹配。

```python
lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)
```
