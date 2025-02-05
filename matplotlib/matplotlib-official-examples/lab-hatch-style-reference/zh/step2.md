# 创建 hatches_plot 函数

hatches_plot 函数将创建一个具有指定阴影线图案的矩形，并将其添加到坐标轴上。它还会添加一个带有阴影线图案的文本。

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
