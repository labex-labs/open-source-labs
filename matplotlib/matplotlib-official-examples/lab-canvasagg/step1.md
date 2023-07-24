# Create a Figure and Canvas

First, we need to create a Figure and a Canvas. The Figure defines the size, shape, and content of the plot, while the Canvas is where the Figure is drawn.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
