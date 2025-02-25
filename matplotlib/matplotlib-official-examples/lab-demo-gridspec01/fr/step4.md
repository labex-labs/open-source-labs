# Annoter les axes

Pour annoter les axes, nous pouvons parcourir les axes de la figure et ajouter du texte en utilisant la fonction `text` et la fonction `tick_params` pour supprimer les étiquettes d'échelonnement.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
