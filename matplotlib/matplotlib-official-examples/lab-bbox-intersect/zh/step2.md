# 设置矩形

我们将使用 `left`、`bottom`、`width` 和 `height` 变量来定义矩形的位置和尺寸。然后，我们将使用 `Rectangle` 类创建矩形，并使用 `add_patch` 方法将其添加到绘图中。

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
