# Graphique conjoint/marginal carré

Il peut être souhaitable d'afficher les distributions marginales à côté d'un graphique de données conjointes. Le code suivant crée un graphique carré avec l'aspect de la boîte des axes marginaux égal aux rapports de largeur et de hauteur de la grille. Cela garantit que tous les axes s'alignent parfaitement, indépendamment de la taille de la figure.

```python
fig5, axs = plt.subplots(2, 2, sharex="col", sharey="row",
                         gridspec_kw=dict(height_ratios=[1, 3],
                                          width_ratios=[3, 1]))
axs[0, 1].set_visible(False)
axs[0, 0].set_box_aspect(1/3)
axs[1, 0].set_box_aspect(1)
axs[1, 1].set_box_aspect(3/1)

np.random.seed(19680801)  # Fixing random state for reproducibility
x, y = np.random.randn(2, 400) * [[.5], [180]]
axs[1, 0].scatter(x, y)
axs[0, 0].hist(x)
axs[1, 1].hist(y, orientation="horizontal")

plt.show()
```
