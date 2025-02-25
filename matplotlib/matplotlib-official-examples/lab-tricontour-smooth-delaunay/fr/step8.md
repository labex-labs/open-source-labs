# Tracer les données

Nous traçons les données affinées à l'aide de la fonction `tricontour` de Matplotlib.

```python
# Options graphiques pour le tracé en ligne de niveau
levels = np.arange(0., 1., 0.025)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_title("Filtrer un maillage de Delaunay\n"
             "(application au tracé en ligne de niveau haute résolution)")

# tracé des contours des données affinées (calculées) :
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='Blues',
              linewidths=[2.0, 0.5, 1.0, 0.5])

plt.show()
```
