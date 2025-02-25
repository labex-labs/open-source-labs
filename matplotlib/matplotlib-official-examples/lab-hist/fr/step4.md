# Personnaliser votre histogramme

Personnaliser un histogramme 2D est similaire au cas 1D, vous pouvez contrôler les composants visuels tels que la taille des boîtes ou la normalisation des couleurs.

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# Nous pouvons augmenter le nombre de boîtes sur chaque axe
axs[0].hist2d(dist1, dist2, bins=40)

# De même que définir la normalisation des couleurs
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# Nous pouvons également définir des nombres personnalisés de boîtes pour chaque axe
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```
