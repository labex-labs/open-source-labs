# 创建一个矩形

我们将通过使用 `matplotlib.patches` 模块中的 `Rectangle()` 函数在绘图中创建一个矩形。创建矩形后，我们将使用 `set_xlim()` 和 `set_ylim()` 函数设置其水平和垂直界限。最后，我们将把矩形添加到绘图中。

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Build a rectangle in axes coords
left, width =.25,.5
bottom, height =.25,.5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Set the horizontal and vertical limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
