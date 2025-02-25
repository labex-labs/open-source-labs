# Interpoler des données en utilisant la méthode linéaire

La deuxième étape consiste à interpoler les données en utilisant la méthode linéaire. Nous allons créer un maillage quadrangulaire régulièrement espacé puis utiliser la méthode LinearTriInterpolator pour interpoler les données. Enfin, nous tracerons les données interpolées.

```python
# Interpoler vers un maillage quadrangulaire régulièrement espacé.
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# Interpoler en utilisant la méthode linéaire.
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# Tracer les données interpolées.
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Linear interpolation")
plt.show()
```
