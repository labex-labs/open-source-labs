# Создание осей для иконки

В этом шаге мы создадим полярную ось, содержащую диаграмму радара Matplotlib.

```python
def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    Создаёт полярную ось, содержащую диаграмму радара matplotlib.

    Параметры
    ----------
    fig : matplotlib.figure.Figure
        Фигура, в которую рисуется.
    ax_position : (float, float, float, float)
        Позиция созданной оси в координатах фигуры в виде
        (x, y, width, height).
    lw_bars : float
        Толщина линий для столбцов.
    lw_grid : float
        Толщина линий для сетки.
    lw_border : float
        Толщина линии границы оси.
    rgrid : array-like
        Позиции радиальной сетки.

    Возвращает
    -------
    ax : matplotlib.axes.Axes
        Созданная ось.
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
            color = *cm.jet(r / 10.)[:3], 0.6  # цвет из jet с alpha=0.6
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # фактический видимый фон - немного выходит за пределы оси
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax
```
