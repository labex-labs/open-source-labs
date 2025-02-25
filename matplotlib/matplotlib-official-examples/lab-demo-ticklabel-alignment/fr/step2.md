# Définir une fonction pour configurer les axes

Pour simplifier le code, nous pouvons définir une fonction qui prend un objet figure et une position en entrée, et renvoie un objet axe avec des étiquettes d'échelle personnalisées.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["court", "trèssss long"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
