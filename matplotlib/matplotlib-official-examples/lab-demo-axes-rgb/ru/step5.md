# Создаем график RGBAxes с отдельными каналами

В этом шаге мы создадим график RGBAxes с отдельными каналами с использованием функции `make_rgb_axes()`. Мы будем использовать метод `imshow()` объектов `Axes` для отображения каналов R, G и B.

```python
def demo_rgb2():
    # Создаем фигуру и объект Axes
    fig, ax = plt.subplots()

    # Создаем объекты Axes для каналов R, G и B с использованием функции make_rgb_axes()
    ax_r, ax_g, ax_b = make_rgb_axes(ax, pad=0.02)

    # Получаем каналы R, G и B и создаем RGB-куб
    r, g, b = get_rgb()
    im_r, im_g, im_b, im_rgb = make_cube(r, g, b)

    # Отображаем RGB-изображение и каналы R, G и B
    ax.imshow(im_rgb)
    ax_r.imshow(im_r)
    ax_g.imshow(im_g)
    ax_b.imshow(im_b)

    # Задаем параметры делений и цвета рамок для всех объектов Axes
    for ax in fig.axes:
        ax.tick_params(direction='in', color='w')
        ax.spines[:].set_color("w")
```
