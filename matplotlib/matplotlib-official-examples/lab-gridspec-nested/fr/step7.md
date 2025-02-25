# Format the Axes

Nous allons formater les axes de tous les sous-graphes à l'aide de la fonction `format_axes`. Cette fonction ajoutera une étiquette de texte à chaque sous-graphe et supprimera les étiquettes d'échelle.

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
