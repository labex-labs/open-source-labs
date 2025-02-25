# Incorporer la transparence

La manière la plus simple d'inclure la transparence lors de la tracé de données avec `imshow` est de passer un tableau correspondant à la forme des données à l'argument `alpha`.

```python
# Créer une canal alpha avec des valeurs croissant linéairement vers la droite.
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# Créer la figure et l'image
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```
