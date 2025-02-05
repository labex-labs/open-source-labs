# 创建图形和画布

首先，我们需要创建一个图形（Figure）和一个画布（Canvas）。图形定义了绘图的大小、形状和内容，而画布则是绘制图形的地方。

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
