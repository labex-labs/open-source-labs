# Создаем график с использованием RGBAxes

В этом шаге мы создадим график с использованием класса `RGBAxes`. Мы будем использовать метод `imshow_rgb()` объекта `RGBAxes` для отображения RGB-изображения.

```python
def demo_rgb1():
    # Создаем фигуру и объект RGBAxes
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)

    # Получаем каналы R, G и B
    r, g, b = get_rgb()

    # Отображаем RGB-изображение с использованием метода imshow_rgb()
    ax.imshow_rgb(r, g, b)
```
