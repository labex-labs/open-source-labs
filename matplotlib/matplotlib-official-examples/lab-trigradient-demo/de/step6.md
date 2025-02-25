# Zeichne die Triangulation, die Potential-Isolinken und das Vektorfeld

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
              linewidths=[2.0, 1.0, 1.0, 1.0])

ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
          units='xy', scale=10., zorder=3, color='blue',
          width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient Plot: Electrical Dipole')
plt.show()
```

Erklärung:

- `fig` und `ax` sind die Figur- und Achsenobjekte respective.
- `ax.set_aspect` setzt das Seitenverhältnis der Achsen.
- `ax.use_sticky_edges` und `ax.margins` setzen die Ränder der Achsen.
- `ax.triplot` zeichnet die Triangulation.
- `ax.tricontour` zeichnet die Potential-Isolinken.
- `ax.quiver` zeichnet das Vektorfeld.
- `ax.set_title` setzt den Titel des Plots.
