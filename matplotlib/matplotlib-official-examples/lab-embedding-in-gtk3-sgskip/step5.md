# Add the Figure to the Scrolled Window

Now we can create a `FigureCanvasGTK3Agg` widget and add it to the scrolled window. This widget will display the Matplotlib figure.

```python
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

canvas = FigureCanvas(fig)
canvas.set_size_request(800, 600)
sw.add(canvas)
```
