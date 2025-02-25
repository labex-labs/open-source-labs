# Создаем диаграмму рассеяния на полярной оси с сдвинутым началом координат

Мы можем создать диаграмму рассеяния на полярной оси с сдвинутым началом координат, установив методы `set_rorigin()` и `set_theta_zero_location()` объекта `PolarAxes`. Мы установим радиус начала координат в `-2,5` и положение нуля угла в `'W'` с сдвигом на `10`.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
