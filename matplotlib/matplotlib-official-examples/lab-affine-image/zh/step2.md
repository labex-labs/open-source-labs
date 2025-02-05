# 创建一个用于绘制图像的函数

在这一步中，我们定义一个函数，该函数将图像、绘图轴和变换作为输入。该函数在绘图轴上以指定的变换显示图像。该函数还会在图像周围显示一个黄色矩形，以展示图像的预期范围。

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
