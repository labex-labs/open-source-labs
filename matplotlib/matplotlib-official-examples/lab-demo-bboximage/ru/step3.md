# Создаем BboxImage для каждой цветовой карты

Далее создаем BboxImage для каждой цветовой карты. Начинаем с создания списка всех цветовых карт с использованием метода `plt.colormaps`. Затем создаем цикл `for`, который перебирает список цветовых карт. Для каждой цветовой карты вычисляем позиции `ix` и `iy` с использованием метода `divmod()`. Затем создаем объект `Bbox` с использованием метода `Bbox.from_bounds()`. Передаем значения `ix`, `iy`, `dx` и `dy` в метод `Bbox.from_bounds()`, чтобы создать ограничивающую рамку. Затем создаем объект `TransformedBbox` с использованием объекта `Bbox` и объекта `ax2.transAxes`. Наконец, создаем объект `BboxImage` с использованием метода `add_artist()`. Передаем объект `TransformedBbox` в конструктор `BboxImage`, чтобы создать изображение с цветовой картой.

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```
