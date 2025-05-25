# Criar uma Figura e uma Tela (Canvas)

Primeiro, precisamos criar uma Figura e uma Tela (Canvas). A Figura define o tamanho, a forma e o conteúdo do gráfico, enquanto a Tela é onde a Figura é desenhada.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
