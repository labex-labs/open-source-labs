# グラフとキャンバスを作成する

まず、グラフとキャンバスを作成する必要があります。グラフはプロットのサイズ、形状、内容を定義します。一方、キャンバスはグラフが描画される場所です。

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```
