# 通过阴影和颜色显示不同变量

在这一步中，你将学习如何通过阴影和颜色显示不同变量。

```python
def shade_other_data():
    """演示如何通过阴影和颜色显示不同变量。"""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z1 = np.sin(x**2)  # 用于生成山体阴影的数据
    z2 = np.cos(x**2 + y**2)  # 用于设置颜色的数据

    norm = Normalize(z2.min(), z2.max())
    cmap = plt.cm.RdBu

    ls = LightSource(315, 45)
    rgb = ls.shade_rgb(cmap(norm(z2)), z1)

    fig, ax = plt.subplots()
    ax.imshow(rgb, interpolation='bilinear')
    ax.set_title('通过一个变量设置阴影，通过另一个变量设置颜色', size='x-large')
```
