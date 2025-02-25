# Créez la classe UpdatingRect

Nous allons créer une sous-classe de Rectangle appelée UpdatingRect. Cette classe est appelée avec une instance Axes, ce qui fait en sorte que le rectangle mette à jour sa forme pour correspondre aux limites de l'Axes.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
