# 方向矢印を追加する

楕円に方向矢印を追加するには、短径の端点にマーカーを描画します。楕円の頂点の座標を取得するには、`get_co_vertices()` メソッドを使用できます。その後、`Affine2D()` クラスを使用して、マーカーを回転させて楕円の角度に一致させることができます。

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Plot an arrow marker at the end point of minor axis
vertices = ellipse.get_co_vertices()
t = Affine2D().rotate_deg(ellipse.angle)
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle(">", "full", t),
    markersize=10
)
```
