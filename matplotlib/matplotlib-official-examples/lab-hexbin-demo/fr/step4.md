# Ajouter une échelle de couleur logarithmique

Nous pouvons ajouter une échelle de couleur logarithmique au graphique à barres hexagonales en définissant `bins='log'` dans `hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Avec une échelle de couleur logarithmique")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```
