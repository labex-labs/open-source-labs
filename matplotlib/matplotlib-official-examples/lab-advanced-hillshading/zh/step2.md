# 在阴影图中避免异常值

在这一步中，你将学习如何使用自定义规范来控制阴影图中显示的z范围。

```python
def avoid_outliers():
    """使用自定义规范来控制阴影图中显示的z范围。"""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z = 10 * np.cos(x**2 + y**2)

    # 添加一些异常值……
    z[100, 105] = 2000
    z[120, 110] = -9000

    ls = LightSource(315, 45)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4.5))

    rgb = ls.shade(z, plt.cm.copper)
    ax1.imshow(rgb, interpolation='bilinear')
    ax1.set_title('完整的数据范围')

    rgb = ls.shade(z, plt.cm.copper, vmin=-10, vmax=10)
    ax2.imshow(rgb, interpolation='bilinear')
    ax2.set_title('手动设置范围')

    fig.suptitle('在阴影图中避免异常值', size='x-large')
```
