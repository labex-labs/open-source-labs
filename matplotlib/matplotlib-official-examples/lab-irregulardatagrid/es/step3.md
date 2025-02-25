# Interpolación en una cuadrícula

Creamos un gráfico de contornos de coordenadas de datos con espaciado irregular a través de la interpolación en una cuadrícula. Primero creamos valores de cuadrícula para x e y utilizando `np.linspace`. Luego interpolamos linealmente los datos (x, y) en una cuadrícula definida por (xi, yi) utilizando `tri.LinearTriInterpolator`. Graficamos los datos interpolados con el habitual `axes.Axes.contour`.

```python
ngridx = 100
ngridy = 200
xi = np.linspace(-2.1, 2.1, ngridx)
yi = np.linspace(-2.1, 2.1, ngridy)

triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

fig, ax1 = plt.subplots()
cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")
ax1.plot(x, y, 'ko', ms=3)
ax1.set(xlim=(-2, 2), ylim=(-2, 2))
ax1.set_title('Contour Plot of Irregularly Spaced Data Interpolated on a Grid')
fig.colorbar(cntr1, ax=ax1)
plt.show()
```
