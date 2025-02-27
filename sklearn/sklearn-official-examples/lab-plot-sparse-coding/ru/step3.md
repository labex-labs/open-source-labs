# Генерация сигнала

Мы сгенерируем сигнал и визуализируем его с использованием Matplotlib.

```python
resolution = 1024
subsampling = 3  # коэффициент субвыборки
width = 100
n_components = resolution // subsampling

# Генерация сигнала
y = np.linspace(0, resolution - 1, resolution)
first_quarter = y < resolution / 4
y[first_quarter] = 3.0
y[np.logical_not(first_quarter)] = -1.0

# Визуализация сигнала
plt.figure()
plt.plot(y)
plt.title("Original Signal")
plt.show()
```
