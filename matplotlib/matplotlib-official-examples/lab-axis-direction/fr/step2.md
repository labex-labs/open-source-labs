# Créer une fonction pour configurer les axes

Nous allons créer une fonction appelée `setup_axes` pour configurer les axes de nos graphiques. Cette fonction prend deux paramètres, un objet `fig` et un objet `pos`. L'objet `fig` est l'objet figure sur lequel nous allons tracer, et l'objet `pos` est la position du sous-graphique dans la figure.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
