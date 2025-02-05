# 创建一个 RGBAxes 绘图

在这一步中，我们将使用 `RGBAxes` 类创建一个 RGBAxes 绘图。我们将使用 `RGBAxes` 对象的 `imshow_rgb()` 方法来显示 RGB 图像。

```python
def demo_rgb1():
    # 创建一个图形和一个 RGBAxes 对象
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)

    # 获取 R、G 和 B 通道
    r, g, b = get_rgb()

    # 使用 imshow_rgb() 方法显示 RGB 图像
    ax.imshow_rgb(r, g, b)
```
