# Créez une fonction pour configurer les axes

Nous allons créer une fonction pour configurer nos axes avec les étiquettes d'échelle souhaitées.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
