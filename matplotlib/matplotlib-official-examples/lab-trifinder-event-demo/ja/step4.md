# カーソルの下の三角形を強調表示する

マウスをプロット上に移動させると、カーソルの下の三角形を強調表示したいと思います。これを行うには、カーソルの下の三角形の頂点で更新される`Polygon`オブジェクトを作成します。`ax.add_patch()`を使用して、ポリゴンをプロットに追加します。

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

また、カーソルの下の三角形の頂点でポリゴンの頂点を更新する`update_polygon()`関数も作成します。

```python
def update_polygon(tri):
    if tri == -1:
        points = [0, 0, 0]
    else:
        points = triang.triangles[tri]
    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))
```
