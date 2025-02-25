# Финальный код

Финальный код объединяет код из шага 1 и шага 2:

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
from mpl_toolkits.axisartist import Axes, HostAxes, angle_helper
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear

def curvelinear_test1(fig):
    # Определяем пользовательское преобразование
    def tr(x, y):
        return x, y - x
    def inv_tr(x, y):
        return x, y + x

    # Создаем объект GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    # Создаем подграфик с пользовательской сеткой и делениями
    ax1 = fig.add_subplot(1, 2, 1, axes_class=Axes, grid_helper=grid_helper)

    # Строим несколько точек на подграфике
    xx, yy = tr(np.array([3, 6]), np.array([5, 10]))
    ax1.plot(xx, yy)

    # Задаем соотношение сторон и пределы подграфика
    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    # Добавляем плавающие оси и сеточные линии
    ax1.axis["t"] = ax1.new_floating_axis(0, 3)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7)
    ax1.grid(True, zorder=0)

def curvelinear_test2(fig):
    # Определяем пользовательское преобразование
    tr = Affine2D().scale(np.pi/180, 1) + PolarAxes.PolarTransform()

    # Определяем экстремум-найтильщик, сеточный локатор и форматтер делений
    extreme_finder = angle_helper.ExtremeFinderCycle(
        nx=20, ny=20,
        lon_cycle=360, lat_cycle=None,
        lon_minmax=None, lat_minmax=(0, np.inf),
    )
    grid_locator1 = angle_helper.LocatorDMS(12)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Создаем объект GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(
        tr, extreme_finder=extreme_finder,
        grid_locator1=grid_locator1, tick_formatter1=tick_formatter1)
    ax1 = fig.add_subplot(
        1, 2, 2, axes_class=HostAxes, grid_helper=grid_helper)

    # Делаем метки делений правой и верхней осей видимыми
    ax1.axis["right"].major_ticklabels.set_visible(True)
    ax1.axis["top"].major_ticklabels.set_visible(True)

    # Позволяем правой оси показывать метки делений для первой координаты (угла)
    ax1.axis["right"].get_helper().nth_coord_ticks = 0

    # Позволяем нижней оси показывать метки делений для второй координаты (радиуса)
    ax1.axis["bottom"].get_helper().nth_coord_ticks = 1

    # Задаем соотношение сторон и пределы подграфика
    ax1.set_aspect(1)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    # Добавляем сеточные линии к подграфику
    ax1.grid(True, zorder=0)

    # Создаем примыкающую ось с заданным преобразованием
    ax2 = ax1.get_aux_axes(tr)

    # Все, что вы рисуете в ax2, будет соответствовать делениям и сетке ax1.
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
