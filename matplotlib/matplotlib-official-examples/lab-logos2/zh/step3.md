# 创建图标轴

在这一步中，我们将创建一个包含 Matplotlib 雷达图的极坐标轴。

```python
def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    创建一个包含 matplotlib 雷达图的极坐标轴。

    参数
    ----------
    fig : matplotlib.figure.Figure
        要绘制到其中的图形。
    ax_position : (float, float, float, float)
        创建的 Axes 在图形坐标中的位置，格式为 (x, y, width, height)。
    lw_bars : float
        条形图的线宽。
    lw_grid : float
        网格的线宽。
    lw_border : float
        Axes 边框的线宽。
    rgrid : 类似数组
        径向网格的位置。

    返回
    -------
    ax : matplotlib.axes.Axes
        创建的 Axes。
    """
    with plt.rc_context({'axes.edgecolor': MPL_BLUE,
                         'axes.linewidth': lw_border}):
        ax = fig.add_axes(ax_position, projection='polar')
        ax.set_axisbelow(True)

        N = 7
        arc = 2. * np.pi
        theta = np.arange(0.0, arc, arc / N)
        radii = np.array([2, 6, 8, 7, 4, 5, 8])
        width = np.pi / 4 * np.array([0.4, 0.4, 0.6, 0.8, 0.2, 0.5, 0.3])
        bars = ax.bar(theta, radii, width=width, bottom=0.0, align='edge',
                      edgecolor='0.3', lw=lw_bars)
        for r, bar in zip(radii, bars):
            color = *cm.jet(r / 10.)[:3], 0.6  # 来自 jet 颜色映射且透明度为 0.6 的颜色
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # 实际可见的背景 - 延伸到轴外一点
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax
```
