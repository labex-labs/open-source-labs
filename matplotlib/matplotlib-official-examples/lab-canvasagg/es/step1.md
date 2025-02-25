# Crear una Figura y un lienzo

En primer lugar, necesitamos crear una Figura y un lienzo. La Figura define el tamaño, la forma y el contenido de la trama, mientras que el lienzo es donde se dibuja la Figura.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
