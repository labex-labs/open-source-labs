# Funktion zum Einrichten der Achsen erstellen

Wir werden eine Funktion namens `setup_axes` erstellen, um die Achsen für unsere Diagramme einzurichten. Diese Funktion nimmt zwei Parameter entgegen, ein `fig`-Objekt und ein `pos`-Objekt. Das `fig`-Objekt ist das Figurobjekt, auf dem wir plotten werden, und das `pos`-Objekt ist die Position des Teilplots innerhalb der Figur.

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
