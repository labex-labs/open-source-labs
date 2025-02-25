# Генерируем объект Path и создаем из него патч

Далее мы сгенерируем объект Path и создадим из него патч. Мы будем использовать объект Path для рисования нашей гистограммы с использованием прямоугольников. Добавьте следующий код:

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
