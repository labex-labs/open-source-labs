# Настраиваем начальный график

Далее настроим начальный график. Создадим синусоидальную волну с частотой 2 Гц с использованием функции `arange` из `numpy`, и построим ее с использованием функции `plot` из `matplotlib.pyplot`.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```
