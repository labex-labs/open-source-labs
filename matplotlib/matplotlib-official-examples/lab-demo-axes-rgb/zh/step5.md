# 创建一个具有单独通道的 RGBAxes 绘图

在这一步中，我们将使用 `make_rgb_axes()` 函数创建一个具有单独通道的 RGBAxes 绘图。我们将使用 `Axes` 对象的 `imshow()` 方法来显示 R、G 和 B 通道。

```python
def demo_rgb2():
    # 创建一个图形和一个 Axes 对象
    fig, ax = plt.subplots()

    # 使用 make_rgb_axes() 函数创建 R、G 和 B Axes 对象
    ax_r, ax_g, ax_b = make_rgb_axes(ax, pad=0.02)

    # 获取 R、G 和 B 通道并创建 RGB 立方体
    r, g, b = get_rgb()
    im_r, im_g, im_b, im_rgb = make_cube(r, g, b)

    # 显示 RGB 图像以及 R、G 和 B 通道
    ax.imshow(im_rgb)
    ax_r.imshow(im_r)
    ax_g.imshow(im_g)
    ax_b.imshow(im_b)

    # 设置所有 Axes 对象的刻度参数和脊柱颜色
    for ax in fig.axes:
        ax.tick_params(direction='in', color='w')
        ax.spines[:].set_color("w")
```
