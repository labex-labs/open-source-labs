# Erstellen eines Diagramms und einer Zeichenfläche

Zunächst müssen wir ein Diagramm und eine Zeichenfläche erstellen. Das Diagramm definiert die Größe, Form und den Inhalt der Grafik, während die Zeichenfläche der Ort ist, an dem das Diagramm gezeichnet wird.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
