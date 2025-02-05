# 创建一个椭圆

接下来，你需要使用 `Ellipse` 类创建一个椭圆。你可以指定椭圆的中心、宽度和高度，以及旋转角度。

```python
from matplotlib.patches import Ellipse

ellipse = Ellipse(
    xy=(2, 4),
    width=30,
    height=20,
    angle=35,
    facecolor="none",
    edgecolor="b"
)
ax.add_patch(ellipse)
```
