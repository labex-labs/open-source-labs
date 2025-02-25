# Créer une figure et une toile

Tout d'abord, nous devons créer une figure et une toile. La figure définit la taille, la forme et le contenu du tracé, tandis que la toile est l'endroit où la figure est dessinée.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
