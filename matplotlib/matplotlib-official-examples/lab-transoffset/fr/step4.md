# Ajout de texte au nuage de points

Maintenant, nous allons ajouter du texte à notre nuage de points en utilisant `offset_copy`. Nous allons tout d'abord créer une transformation qui positionne le texte à un décalage spécifié dans les coordonnées d'écran par rapport à un emplacement donné dans n'importe quelles coordonnées. Ensuite, nous utiliserons la fonction `text` de `matplotlib.pyplot` pour ajouter le texte au graphique.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
