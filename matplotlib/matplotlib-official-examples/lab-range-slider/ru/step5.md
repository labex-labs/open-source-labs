# Создать функцию обратного вызова для ползунка

Мы создадим функцию обратного вызова, которая будет вызываться каждый раз, когда пользователь изменяет значения порога с использованием ползунка. Функция обновит карту цветов изображения и позиции вертикальных линий на гистограмме.

```python
def update(val):
    # The val passed to a callback by the RangeSlider will
    # be a tuple of (min, max)

    # Update the image's colormap
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Update the position of the vertical lines
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Redraw the figure to ensure it updates
    fig.canvas.draw_idle()


slider.on_changed(update)
```
