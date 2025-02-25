# Полярная проекция в прямоугольной области

Далее мы создадим полярную проекцию в прямоугольной области с использованием `GridHelperCurveLinear`. Мы будем использовать преобразование `Affine2D` для масштабирования градусных координат до радиан, и `PolarAxes.PolarTransform` для создания полярной проекции. Также мы будем использовать `angle_helper.ExtremeFinderCycle` для нахождения экстремумов полярной проекции, и `angle_helper.LocatorDMS` и `angle_helper.FormatterDMS` для форматирования меток делений. Следующий код демонстрирует этот процесс:

```python
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
curvelinear_test2(fig)
plt.show()
```
