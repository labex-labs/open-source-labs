# Créer un tracé et une barre de couleur pour les données positives

Nous créons un tracé des données positives et ajoutons une barre de couleur au tracé en utilisant la fonction `colorbar`.

```python
# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = plt.imshow(Zpos, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
plt.colorbar(pos)
```
