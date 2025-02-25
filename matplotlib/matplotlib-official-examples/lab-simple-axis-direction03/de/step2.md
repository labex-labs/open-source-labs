# Achsenfunktion einrichten

Erstellen Sie eine Funktion, um die Achsen einzurichten. Diese Funktion wird die x- und y-Markierungswerte festlegen.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
