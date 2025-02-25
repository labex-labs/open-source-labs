# Полярные оси (Polar Axes)

Мы можем создать сетку полярных осях (`Axes`), передав параметр `projection='polar'` в функцию `subplots()`.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
