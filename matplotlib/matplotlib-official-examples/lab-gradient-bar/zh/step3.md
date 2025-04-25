# 定义渐变图像函数

我们需要定义一个函数，该函数将基于颜色映射表创建一个渐变图像。此函数将接受一个坐标轴对象、渐变方向以及要使用的颜色映射表范围。然后，该函数将生成渐变图像并返回它。

```python
def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    根据颜色映射表绘制渐变图像。

    参数
    ----------
    ax : Axes
        要绘制的坐标轴。
    direction : float
        渐变方向。这是一个介于 0（=垂直）到 1（=水平）之间的数字。
    cmap_range : float, float
        颜色映射表中应用于渐变的部分（cmin, cmax），其中完整的颜色映射表范围是 (0, 1)。
    **kwargs
        其他参数将传递给 `.Axes.imshow()`。
        特别是，*cmap*、*extent*和*transform*可能会很有用。
    """
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, interpolation='bicubic', clim=(0, 1),
                   aspect='auto', **kwargs)
    return im
```
