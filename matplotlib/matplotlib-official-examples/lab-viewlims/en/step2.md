# Create the UpdatingRect class

We will create a subclass of Rectangle called UpdatingRect. This class is called with an Axes instance, causing the rectangle to update its shape to match the bounds of the Axes.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
