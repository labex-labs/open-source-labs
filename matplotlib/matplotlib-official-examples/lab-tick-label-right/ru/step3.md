# Создаем примерный график

Построим примерный график, чтобы увидеть, как он выглядит с метками делений по оси y справа.

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
