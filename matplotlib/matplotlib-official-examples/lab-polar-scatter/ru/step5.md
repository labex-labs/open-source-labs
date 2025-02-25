# Создаем диаграмму рассеяния на полярной оси, ограниченной сектором

Мы можем создать диаграмму рассеяния на полярной оси, ограниченной сектором, установив методы `set_thetamin()` и `set_thetamax()` объекта `PolarAxes`. Мы установим начальное и конечное ограничения угла в `45` и `135` соответственно.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
