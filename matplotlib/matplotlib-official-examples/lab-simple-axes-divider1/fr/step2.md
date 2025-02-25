# Définition d'une fonction d'aide

Nous allons définir une fonction d'aide `label_axes()` qui sera utilisée pour placer une étiquette au centre d'un axe et supprimer les graduations de l'axe.

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5,.5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
