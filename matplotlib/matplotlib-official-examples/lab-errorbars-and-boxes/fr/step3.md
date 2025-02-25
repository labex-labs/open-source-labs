# Créer une fonction pour les boîtes d'erreur

Nous allons maintenant créer une fonction appelée `make_error_boxes` qui créera le patch rectangulaire défini par les limites des barres dans les directions x et y.

```python
def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='none', alpha=0.5):

    # Boucle sur les points de données ; créer une boîte à partir des erreurs à chaque point
    errorboxes = [Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
                  for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)]

    # Créer une collection de patches avec la couleur/alpha spécifiée
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)

    # Ajouter la collection aux axes
    ax.add_collection(pc)

    # Tracer les barres d'erreur
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='none', ecolor='k')

    return artists
```
