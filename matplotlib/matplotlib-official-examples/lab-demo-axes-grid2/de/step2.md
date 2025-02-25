# Definieren einer Funktion zum Hinzufügen von inneren Titeln zu den Achsen

Die Funktion `add_inner_title` wird verwendet, um Titeln zu den Bildern hinzuzufügen.

```python
def add_inner_title(ax, title, loc, **kwargs):
    from matplotlib.offsetbox import AnchoredText
    from matplotlib.patheffects import withStroke
    prop = dict(path_effects=[withStroke(foreground='w', linewidth=3)],
                size=plt.rcParams['legend.fontsize'])
    at = AnchoredText(title, loc=loc, prop=prop,
                      pad=0., borderpad=0.5,
                      frameon=False, **kwargs)
    ax.add_artist(at)
    return at
```
