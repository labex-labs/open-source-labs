# Création du tracé

Dans cette étape, nous allons créer le graphe de niveau masqué à l'aide de la fonction `contourf()`. Nous passons les tableaux `x`, `y` et `z` à cette fonction, ainsi que l'argument `corner_mask` défini sur `True` ou `False` selon le type de graphe que nous souhaitons créer.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Tracer la grille.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indiquer les points masqués avec des cercles rouges.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
