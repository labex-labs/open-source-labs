# Создание данных

В этом шаге мы создадим некоторые данные для визуализации. Мы создадим точечный график точек на сетке.

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
