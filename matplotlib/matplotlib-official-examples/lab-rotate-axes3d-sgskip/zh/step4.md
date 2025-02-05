# 旋转轴并更新绘图

最后，我们将使用一个for循环来旋转轴并更新绘图，该循环会遍历仰角、方位角、滚动角以及全方位的完整旋转。我们将使用 `ax.view_init()` 函数来更新轴视图和标题，并使用 `plt.title()`、`plt.draw()` 和 `plt.pause()` 函数来显示动画。

```python
# Rotate the axes and update the plot
for angle in range(0, 360*4 + 1):
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all
    elev = azim = roll = 0
    if angle <= 360:
        elev = angle_norm
    elif angle <= 360*2:
        azim = angle_norm
    elif angle <= 360*3:
        roll = angle_norm
    else:
        elev = azim = roll = angle_norm

    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

    # Display animation
    plt.draw()
    plt.pause(.001)
```
