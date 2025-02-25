# Используем граничную норму

Вместо этого мы будем использовать граничную норму для окрашивания отрезков прямой. Создадим `ListedColormap`, содержащий три цвета - красный, зеленый и синий. Затем создадим `BoundaryNorm` с границами -1, -0,5, 0,5 и 1, а также `ListedColormap`. Используем функцию `set_array` для установки значений, используемых для отображения цветов.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
