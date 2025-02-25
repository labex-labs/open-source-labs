# Tracer la triangulation, les lignes d'iso-potentiel et le champ vectoriel

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

Explication :

- `fig` et `ax` sont respectivement les objets figure et axes.
- `ax.set_aspect` définit le rapport d'aspect des axes.
- `ax.use_sticky_edges` et `ax.margins` définissent les marges des axes.
- `ax.triplot` trace la triangulation.
- `ax.tricontour` trace les lignes d'iso-potentiel.
- `ax.quiver` trace le champ vectoriel.
- `ax.set_title` définit le titre du tracé.
