# Генерируем данные

В этом шаге мы генерируем некоторые данные для использования в графике. Мы создадим гауссовский цветной шум с использованием функции `convolve` из NumPy и построим его с использованием Matplotlib.

```python
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

fig, main_ax = plt.subplots()
main_ax.plot(t, s)
```
