# 最终代码

最终代码结合了步骤 1 和步骤 2 中的代码：

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
from mpl_toolkits.axisartist import Axes, HostAxes, angle_helper
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear

def curvelinear_test1(fig):
    # 定义自定义变换
    def tr(x, y):
        return x, y - x
    def inv_tr(x, y):
        return x, y + x

    # 创建 GridHelperCurveLinear 对象
    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    # 创建一个带有自定义网格和刻度线的子图
    ax1 = fig.add_subplot(1, 2, 1, axes_class=Axes, grid_helper=grid_helper)

    # 在子图上绘制一些点
    xx, yy = tr(np.array([3, 6]), np.array([5, 10]))
    ax1.plot(xx, yy)

    # 设置子图的纵横比和限制
    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    # 添加浮动轴和网格线
    ax1.axis["t"] = ax1.new_floating_axis(0, 3)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7)
    ax1.grid(True, zorder=0)

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
curvelinear_test1(fig)
curvelinear_test2(fig)
plt.show()
```
