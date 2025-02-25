# Interpolation sur une grille

Nous créons un tracé de contour des coordonnées de données à espacement irrégulier par interpolation sur une grille. Nous créons d'abord des valeurs de grille pour x et y en utilisant `np.linspace`. Nous interpolons ensuite linéairement les données (x, y) sur une grille définie par (xi, yi) en utilisant `tri.LinearTriInterpolator`. Nous traçons les données interpolées avec le contour habituel `axes.Axes.contour`.

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
