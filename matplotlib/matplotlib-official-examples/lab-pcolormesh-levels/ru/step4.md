# Создание уровней с использованием нормативных значений

Показывает, как комбинировать экземпляры Нормализации и Колормапы для рисования "уровней" в типах графиков `.axes.Axes.pcolor`, `.axes.Axes.pcolormesh` и `.axes.Axes.imshow` аналогично аргументу ключевого слова levels для contour/contourf.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# сделайте эти значения меньше, чтобы увеличить разрешение
dx, dy = 0.05, 0.05

# сгенерируйте 2 двумерных сетки для границ x и y
y, x = np.mgrid[slice(1, 5 + dy, dy),
                slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x и y - это границы, поэтому z должен быть значением *внутри* этих границ.
# Поэтому удалите последнее значение из массива z.
z = z[:-1, :-1]
уровни = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# выберите желаемую карту цветов, разумные уровни и определите экземпляр
# нормализации, который берет значения данных и преобразует их в уровни.
cmap = plt.colormaps['PiYG']
norm = BoundaryNorm(уровни, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh с уровнями')


# контуры - это графики *по точкам*, поэтому преобразуйте наши границы в
# центры точек
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=уровни,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf с уровнями')

# уточните расстояние между подграфиками, чтобы надпись `ax1` и метки
# делений `ax0` не пересекались
fig.tight_layout()

plt.show()
```
