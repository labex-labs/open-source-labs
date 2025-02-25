# Interpolar datos usando el método cúbico

El tercer paso es interpolar los datos usando el método cúbico. Usaremos el método CubicTriInterpolator con el parámetro kind establecido en 'geom' o'min_E'. Finalmente, graficaremos los datos interpolados.

```python
# Interpolar usando el método cúbico con kind=geom.
interp_cubic_geom = mtri.CubicTriInterpolator(triang, z, kind='geom')
zi_cubic_geom = interp_cubic_geom(xi, yi)

# Graficar los datos interpolados.
plt.contourf(xi, yi, zi_cubic_geom)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='geom'")
plt.show()

# Interpolar usando el método cúbico con kind=min_E.
interp_cubic_min_E = mtri.CubicTriInterpolator(triang, z, kind='min_E')
zi_cubic_min_E = interp_cubic_min_E(xi, yi)

# Graficar los datos interpolados.
plt.contourf(xi, yi, zi_cubic_min_E)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='min_E'")
plt.show()
```
