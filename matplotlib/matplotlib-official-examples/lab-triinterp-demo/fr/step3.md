# Interpoler des données en utilisant la méthode cubique

La troisième étape consiste à interpoler les données en utilisant la méthode cubique. Nous allons utiliser la méthode CubicTriInterpolator avec le paramètre kind défini sur 'geom' ou'min_E'. Enfin, nous tracerons les données interpolées.

```python
# Interpoler en utilisant la méthode cubique avec kind=geom.
interp_cubic_geom = mtri.CubicTriInterpolator(triang, z, kind='geom')
zi_cubic_geom = interp_cubic_geom(xi, yi)

# Tracer les données interpolées.
plt.contourf(xi, yi, zi_cubic_geom)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='geom'")
plt.show()

# Interpoler en utilisant la méthode cubique avec kind=min_E.
interp_cubic_min_E = mtri.CubicTriInterpolator(triang, z, kind='min_E')
zi_cubic_min_E = interp_cubic_min_E(xi, yi)

# Tracer les données interpolées.
plt.contourf(xi, yi, zi_cubic_min_E)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='min_E'")
plt.show()
```
