# Создаем функцию для отображения изображения

В этом шаге мы определяем функцию, которая принимает на вход изображение, ось для отображения и преобразование. Функция отображает изображение на оси для отображения с указанным преобразованием. Функция также отображает желтый прямоугольник вокруг изображения, чтобы показать предполагаемый диапазон изображения.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
