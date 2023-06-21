# Interpolation on a grid

We create a contour plot of irregularly spaced data coordinates via interpolation on a grid. We first create grid values for x and y using `np.linspace`. We then linearly interpolate the data (x, y) on a grid defined by (xi, yi) using `tri.LinearTriInterpolator`. We plot the interpolated data with the usual `axes.Axes.contour`.

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

#
