# Создаем коллекцию эллипсов

Создаем `EllipseCollection` с помощью вышеуказанных данных и указываем, что единицы измерения - 'x', а смещения - `XY`.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
