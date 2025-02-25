# グラフ座標で中央に配置されたインセットを作成する

`blended_transform_factory()` メソッドを使って混合変換を作成し、それを `bbox_transform` パラメータとして使用することで、グラフ座標で水平方向に中央に配置され、垂直方向には軸と整列するように制限されたインセットを作成できます。

```python
# グラフ座標で水平方向に中央に配置され、垂直方向には軸と整列するように制限されたインセットを作成する。
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
