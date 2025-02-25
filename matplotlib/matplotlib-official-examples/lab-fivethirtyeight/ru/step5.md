# Строим график данных

В этом шаге мы построим график данных на объекте Axes с использованием функции `plot` из Matplotlib. Мы построим шесть разных линий с разными наклонами и случайным шумом.

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```
