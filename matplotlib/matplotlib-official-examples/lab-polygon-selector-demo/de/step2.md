# Daten erstellen

In diesem Schritt werden wir einige Daten erstellen, um sie zu visualisieren. Wir werden einen Streudiagramm von Punkten auf einem Gitter erstellen.

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
