# Erstellen der Klasse UpdatingRect

Wir werden eine Unterklasse von Rectangle namens UpdatingRect erstellen. Diese Klasse wird mit einer Axes-Instanz aufgerufen, was dazu führt, dass das Rechteck seine Form aktualisiert, um den Grenzen der Axes zu entsprechen.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
