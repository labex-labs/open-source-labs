# Erstellen einer Funktion zum Einrichten der Achsen

Wir werden eine Funktion erstellen, um unsere Achsen mit den gewünschten Skalenbeschriftungen einzurichten.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
