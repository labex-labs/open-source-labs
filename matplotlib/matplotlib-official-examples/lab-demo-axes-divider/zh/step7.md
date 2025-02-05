# 绘图

在这一步中，我们将创建一个图形，并为我们要创建的每个图像添加子图。

```python
def demo():
    fig = plt.figure(figsize=(6, 6))

    # 图1
    # 简单图像和颜色条
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)

    # 图2
    # 绘制时定位的图像和颜色条 - 一种复杂的方法
    demo_locatable_axes_hard(fig)

    # 图3
    # 绘制时定位的图像和颜色条 - 一种简单的方法
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)

    # 图4
    # 带有固定间距的并排双图像。
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)

    plt.show()
```
