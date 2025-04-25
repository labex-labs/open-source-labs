# 塗りつぶした領域を作成する

`Polygon`パッチを使って塗りつぶした領域を作成します。`linspace`と手順 1 で定義した関数を使って領域の x と y の値を生成します。そして、領域の頂点をタプルのリストとして定義します。最後に、`Polygon`オブジェクトを作成し、`add_patch`を使って軸に追加します。

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
