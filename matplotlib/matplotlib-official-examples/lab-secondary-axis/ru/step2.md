# Построим график данных

Создадим простой синусоидальный сигнал, чтобы продемонстрировать применение вторичной оси. Построим синусоидальный сигнал, используя градусы в качестве оси x.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```
