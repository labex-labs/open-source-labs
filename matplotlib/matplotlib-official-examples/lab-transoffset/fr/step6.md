# Ajout de texte au graphique polaire

Enfin, nous allons ajouter du texte à notre graphique polaire en utilisant `offset_copy` et la fonction `text` de `matplotlib.pyplot`.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       y=6, units='dots')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)),
             transform=trans_offset,
             horizontalalignment='center',
             verticalalignment='bottom')
```
