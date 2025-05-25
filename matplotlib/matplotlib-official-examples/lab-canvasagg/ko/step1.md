# Figure 및 Canvas 생성

먼저 Figure 와 Canvas 를 생성해야 합니다. Figure 는 플롯의 크기, 모양 및 내용을 정의하고, Canvas 는 Figure 가 그려지는 곳입니다.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
