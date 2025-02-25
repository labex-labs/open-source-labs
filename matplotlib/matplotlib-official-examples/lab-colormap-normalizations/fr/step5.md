# BoundaryNorm

Nous allons fournir des limites pour les couleurs en utilisant `BoundaryNorm`.

```python
fig, ax = plt.subplots(3, 1, figsize=(8, 8))
ax = ax.flatten()
bounds = np.linspace(-1, 1, 10)
norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
pcm = ax[0].pcolormesh(X, Y, Z,
                       norm=norm,
                       cmap='RdBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[0], extend='both', orientation='vertical')

bounds = np.array([-0.25, -0.125, 0, 0.5, 1])
norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
pcm = ax[1].pcolormesh(X, Y, Z, norm=norm, cmap='RdBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[1], extend='both', orientation='vertical')

pcm = ax[2].pcolormesh(X, Y, Z, cmap='RdBu_r', vmin=-np.max(Z1),
                       shading='nearest')
fig.colorbar(pcm, ax=ax[2], extend='both', orientation='vertical')

plt.show()
```
