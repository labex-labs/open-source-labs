# Interpolação em uma grade

Criamos um gráfico de contorno de coordenadas de dados espaçados irregularmente via interpolação em uma grade. Primeiro, criamos valores de grade para x e y usando `np.linspace`. Em seguida, interpolamos linearmente os dados (x, y) em uma grade definida por (xi, yi) usando `tri.LinearTriInterpolator`. Plotamos os dados interpolados com o `axes.Axes.contour` usual.

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
