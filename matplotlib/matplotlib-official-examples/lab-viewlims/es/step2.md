# Crear la clase UpdatingRect

Crearemos una subclase de Rectangle llamada UpdatingRect. Esta clase se llama con una instancia de Axes, lo que hace que el rectángulo actualice su forma para que coincida con los límites del Axes.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
