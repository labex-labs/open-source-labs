# Создайте функцию для настройки осей

Мы создадим функцию под названием `setup_axes`, чтобы настроить оси для наших графиков. Эта функция принимает два параметра: объект `fig` и объект `pos`. Объект `fig` - это объект фигуры, на которой мы будем рисовать, а объект `pos` - это позиция подграфика внутри фигуры.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
