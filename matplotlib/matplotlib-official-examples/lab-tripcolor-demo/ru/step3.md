# Создать график tripcolor

Теперь мы создадим график tripcolor с использованием функции `tripcolor()`. Мы создадим два графика с использованием различных методов оттенков.

```python
# График с плоским оттенкованием
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

# График с оттенкованием Гуро
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
tpc = ax2.tripcolor(triang, z, shading='gouraud')
fig2.colorbar(tpc)
ax2.set_title('tripcolor of Delaunay triangulation, gouraud shading')
```
