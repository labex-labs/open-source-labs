# Создаем график

Теперь мы можем создать график с использованием функции `plt.subplots()`. Также мы создадим три линии с использованием функции `ax.plot()`.

```python
fig, ax = plt.subplots()

# Используем set_dashes() и set_capstyle() для изменения пунктира существующей линии.
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt линия, 2pt перерыв, 10pt линия, 2pt перерыв.
line1.set_dash_capstyle('round')

# Используем plot(..., dashes=...) для установки пунктира при создании линии.
line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

# Используем plot(..., dashes=..., gapcolor=...) для установки пунктира и
# чередующихся цветов при создании линии.
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')

ax.legend(handlelength=4)
plt.show()
```
