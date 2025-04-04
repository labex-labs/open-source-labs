# Tracé des hachures sans couleur avec une légende

Dans cette étape, nous allons créer un tracé des hachures sans couleur et ajouter une légende. Nous utiliserons la fonction `contour` pour créer les lignes de niveau et la fonction `contourf` pour spécifier les hachures sans couleur.

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```
