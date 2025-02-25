# Créer un Sélecteur de plage

Nous allons créer un objet Sélecteur de plage à l'aide de `matplotlib.widgets.SpanSelector`.

```python
span = SpanSelector(
    ax1,
    onselect,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:blue"),
    interactive=True,
    drag_from_anywhere=True
)
```
