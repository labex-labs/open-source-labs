# Utiliser la transparence pour souligner les valeurs

Enfin, nous allons recréer le même tracé, mais cette fois-ci, nous utiliserons la transparence pour souligner les valeurs extrêmes dans les données. Cela est souvent utilisé pour souligner les points de données avec des p-valeurs plus petites. Nous ajouterons également des lignes de contour pour souligner les valeurs de l'image.

```python
# Créer un canal alpha basé sur les valeurs de poids
alphas = Normalize(0,.3, clip=True)(np.abs(weights))
alphas = np.clip(alphas,.4, 1)  # valeur d'alpha limitée en bas à.4

# Créer la figure et l'image
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# Ajouter des lignes de contour pour souligner davantage différents niveaux.
ax.contour(weights[::-1], levels=[-.1,.1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001,.0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
