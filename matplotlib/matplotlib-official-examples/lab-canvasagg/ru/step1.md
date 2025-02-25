# Создание фигуры и холста

Во - первых, нам нужно создать фигуру (`Figure`) и холст (`Canvas`). Фигура определяет размер, форму и содержимое графика, а холст - это место, где рисуется фигура.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
