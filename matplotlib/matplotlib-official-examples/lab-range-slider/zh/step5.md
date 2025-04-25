# 为滑块创建一个回调函数

我们将创建一个回调函数，每当用户使用滑块更改阈值时，该函数就会被调用。该函数将更新图像的颜色映射以及直方图上垂直线的位置。

```python
def update(val):
    # 由 RangeSlider 传递给回调的 val
    # 将是一个 (min, max) 元组

    # 更新图像的颜色映射
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # 更新垂直线的位置
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # 重绘图形以确保更新
    fig.canvas.draw_idle()


slider.on_changed(update)
```
