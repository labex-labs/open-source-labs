# 定义 `confidence_ellipse` 函数

接下来，我们定义 `confidence_ellipse` 函数，该函数将接受数据集的 x 和 y 坐标、用于绘制椭圆的坐标轴对象以及标准差的数量。它返回一个表示椭圆的 Matplotlib 补丁对象。

```python
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    创建 *x* 和 *y* 的协方差置信椭圆的绘图。

    参数
    ----------
    x, y : 类似数组，形状 (n, )
        输入数据。

    ax : matplotlib.axes.Axes
        要在其中绘制椭圆的坐标轴对象。

    n_std : 浮点数
        用于确定椭圆半径的标准差数量。

    **kwargs
        转发给 `~matplotlib.patches.Ellipse`

    返回
    -------
    matplotlib.patches.Ellipse
    """
    if x.size!= y.size:
        raise ValueError("x 和 y 必须大小相同")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # 使用特殊情况获取此二维数据集的特征值。
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # 根据方差的平方根计算 x 的标准差，并乘以给定的标准差数量。
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # 计算 y 的标准差...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
     .rotate_deg(45) \
     .scale(scale_x, scale_y) \
     .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
```
