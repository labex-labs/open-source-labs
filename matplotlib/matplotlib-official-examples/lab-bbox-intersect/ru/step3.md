# Генерируем случайные линии

Мы сгенерируем 12 случайных линий с использованием библиотеки `numpy` и построим их с использованием метода `plot`. Если линия пересекает прямоугольник, ее цвет будет красным, в противном случае - синим. Мы будем использовать класс `Path` для создания линии и метод `intersects_bbox` для проверки, пересекает ли она прямоугольник.

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
