# Сетка для пользовательского преобразования

Сначала мы создадим пользовательскую сетку и деления с использованием `GridHelperCurveLinear`. Пользовательское преобразование будет применяться к сетке и делениям. Следующий код демонстрирует этот процесс:

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

fig = plt.figure(figsize=(7, 4))
curvelinear_test1(fig)
plt.show()
```
