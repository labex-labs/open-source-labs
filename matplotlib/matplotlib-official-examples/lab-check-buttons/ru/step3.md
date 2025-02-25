# Создание графика

Теперь мы создадим график с использованием `matplotlib`. Мы построим три синусоиды на одном графике и установим видимость первой волны в `False`, так как мы хотим, чтобы она была скрытой изначально.

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```
