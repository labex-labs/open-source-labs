# Создание логотипа

В этом шаге мы создадим полную фигуру с логотипом Matplotlib.

```python
def make_logo(height_px, lw_bars, lw_grid, lw_border, rgrid, with_text=False):
    """
    Создаёт полную фигуру с логотипом Matplotlib.

    Параметры
    ----------
    height_px : int
        Высота фигуры в пикселях.
    lw_bars : float
        Толщина линии границы столбцов.
    lw_grid : float
        Толщина линии сетки.
    lw_border : float
        Толщина линии границы иконки.
    rgrid : sequence of float
        Позиции радиальной сетки.
    with_text : bool
        Рисовать только иконку или включать слово 'matplotlib' в виде текста.
    """
    dpi = 100
    height = height_px / dpi
    figsize = (5 * height, height) если with_text иначе (height, height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)

    если with_text:
        create_text_axes(fig, height_px)
    ax_pos = (0.535, 0.12,.17, 0.75) если with_text иначе (0.03, 0.03,.94,.94)
    ax = create_icon_axes(fig, ax_pos, lw_bars, lw_grid, lw_border, rgrid)

    return fig, ax
```
