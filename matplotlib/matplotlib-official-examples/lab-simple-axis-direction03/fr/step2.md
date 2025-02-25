# Fonction de configuration des axes

Créer une fonction pour configurer les axes. Cette fonction définira les valeurs d'échelle sur l'axe x et y.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
