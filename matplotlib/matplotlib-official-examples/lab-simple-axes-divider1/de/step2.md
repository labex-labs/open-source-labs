# Definition einer Hilfsfunktion

Wir werden eine Hilfsfunktion `label_axes()` definieren, die verwendet werden soll, um eine Bezeichnung in der Mitte einer Achse zu platzieren und die Achsenmarkierungen zu entfernen.

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5,.5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
