# 定义设置轴的函数

接下来，定义`setup_axes()`函数，该函数用于设置图表的极坐标投影。此函数使用`GridHelperCurveLinear`在矩形框中创建极坐标投影。它还设置了图表的界限并返回`ax1`对象。

```python
def setup_axes(fig, rect):
    # 定义极坐标轴变换和极值查找器
    tr = Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()
    extreme_finder = angle_helper.ExtremeFinderCycle(20, 20, lon_cycle=360, lat_cycle=None, lon_minmax=None, lat_minmax=(0, np.inf))

    # 定义网格定位器和格式化器
    grid_locator1 = angle_helper.LocatorDMS(12)
    grid_locator2 = grid_finder.MaxNLocator(5)
    tick_formatter1 = angle_helper.FormatterDMS()

    # 定义 GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(tr, extreme_finder=extreme_finder, grid_locator1=grid_locator1, grid_locator2=grid_locator2, tick_formatter1=tick_formatter1)

    # 创建轴对象并设置其界限
    ax1 = fig.add_subplot(rect, axes_class=axisartist.Axes, grid_helper=grid_helper)
    ax1.axis[:].set_visible(False)
    ax1.set_aspect(1.)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    return ax1
```
