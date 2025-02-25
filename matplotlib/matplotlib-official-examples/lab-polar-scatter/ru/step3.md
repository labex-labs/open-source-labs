# Создаем диаграмму рассеяния на полярной оси

Мы создадим диаграмму рассеяния на полярной оси с использованием функции `plt.scatter()`. Мы установим параметр `projection` в `'polar'` и передадим значения радиуса, угла, цвета и площади в качестве параметров.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
