# 矩形框中的极坐标投影

接下来，我们将使用 `GridHelperCurveLinear` 在矩形框中创建极坐标投影。我们将使用 `Affine2D` 变换将角度坐标缩放到弧度，并使用 `PolarAxes.PolarTransform` 创建极坐标投影。我们还将使用 `angle_helper.ExtremeFinderCycle` 来找到极坐标投影的极值，并使用 `angle_helper.LocatorDMS` 和 `angle_helper.FormatterDMS` 来格式化刻度标签。以下代码演示了这个过程：

```python
def curvelinear_test2(fig):
    # 定义自定义变换
    tr = Affine2D().scale(np.pi/180, 1) + PolarAxes.PolarTransform()

    # 定义极值查找器、网格定位器和刻度格式化器
    extreme_finder = angle_helper.ExtremeFinderCycle(
        nx=20, ny=20,
        lon_cycle=360, lat_cycle=None,
        lon_minmax=None, lat_minmax=(0, np.inf),
    )
    grid_locator1 = angle_helper.LocatorDMS(12)
    tick_formatter1 = angle_helper.FormatterDMS()

    # 创建 GridHelperCurveLinear 对象
    grid_helper = GridHelperCurveLinear(
        tr, extreme_finder=extreme_finder,
        grid_locator1=grid_locator1, tick_formatter1=tick_formatter1)
    ax1 = fig.add_subplot(
        1, 2, 2, axes_class=HostAxes, grid_helper=grid_helper)

    # 使右侧和顶部轴的刻度标签可见
    ax1.axis["right"].major_ticklabels.set_visible(True)
    ax1.axis["top"].major_ticklabels.set_visible(True)

    # 让右侧轴显示第一个坐标（角度）的刻度标签
    ax1.axis["right"].get_helper().nth_coord_ticks = 0

    # 让底部轴显示第二个坐标（半径）的刻度标签
    ax1.axis["bottom"].get_helper().nth_coord_ticks = 1

    # 设置子图的纵横比和限制
    ax1.set_aspect(1)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    # 向子图添加网格线
    ax1.grid(True, zorder=0)

    # 使用给定的变换创建一个寄生轴
    ax2 = ax1.get_aux_axes(tr)

    # 在 ax2 中绘制的任何内容都将与 ax1 的刻度和网格匹配。
    ax2.plot(np.linspace(0, 30, 51), np.linspace(10, 10, 51), linewidth=2)

    ax2.pcolor(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
               np.arange(9).reshape((3, 3)))
    ax2.contour(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
                np.arange(16).reshape((4, 4)), colors="k")

fig = plt.figure(figsize=(7, 4))
curvelinear_test2(fig)
plt.show()
```
