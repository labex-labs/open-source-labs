# Создание гистограммы

Теперь, когда у нас есть наши данные, мы можем создать трехмерную гистограмму. Мы будем использовать функцию `histogram2d()` из NumPy для создания двумерной гистограммы наших данных, а затем функцию `bar3d()` из Matplotlib для создания трехмерной гистограммы столбцов.

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```
