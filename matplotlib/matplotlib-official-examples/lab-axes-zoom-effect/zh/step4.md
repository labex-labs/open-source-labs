# 连接轴

在这一步中，我们将连接轴并创建缩放效果。我们将创建一个包含四个轴的图形，并使用 zoom_effect01 和 zoom_effect02 函数将它们连接起来。

```python
axs = plt.figure().subplot_mosaic([
    ["zoom1", "zoom2"],
    ["main", "main"],
])

axs["main"].set(xlim=(0, 5))
zoom_effect01(axs["zoom1"], axs["main"], 0.2, 0.8)
axs["zoom2"].set(xlim=(2, 3))
zoom_effect02(axs["zoom2"], axs["main"])

plt.show()
```
