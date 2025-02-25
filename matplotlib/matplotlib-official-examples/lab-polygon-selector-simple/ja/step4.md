# すべてをまとめる

プログラムで多角形を作成することと対話的に多角形を作成することの両方を含む完全なサンプルを作成しましょう。

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# グラフと軸を作成する
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# PolygonSelectorオブジェクトを作成して頂点を追加する
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# 多角形を描画する
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# 対話的作成用の別のPolygonSelectorオブジェクトを作成する
selector2 = PolygonSelector(ax2, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

plt.show()
```
