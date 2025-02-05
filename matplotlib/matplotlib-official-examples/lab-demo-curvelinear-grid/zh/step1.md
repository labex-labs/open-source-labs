# 自定义变换的网格

首先，我们将使用 `GridHelperCurveLinear` 创建一个自定义网格和刻度线。自定义变换将应用于网格和刻度线。以下代码演示了这个过程：

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

fig = plt.figure(figsize=(7, 4))
curvelinear_test1(fig)
plt.show()
```
