# 将自定义框样式实现为函数

自定义框样式可以实现为函数，这些函数接受指定矩形框和“变形”量的参数，并返回“变形”后的路径。在这里，我们将实现一种自定义框样式，它返回一个新路径，该路径在框的左侧添加一个“箭头”形状。

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    给定框的位置和大小，返回围绕它的框的路径。

    旋转会自动处理。

    参数
    ----------
    x0, y0, width, height : float
        框的位置和大小。
    mutation_size : float
        变形参考比例，通常是文本字体大小。
    """
    # 填充
    mypad = 0.3
    pad = mutation_size * mypad
    # 添加填充后的宽度和高度。
    width = width + 2 * pad
    height = height + 2 * pad
    # 填充后框的边界
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # 返回新路径
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```
