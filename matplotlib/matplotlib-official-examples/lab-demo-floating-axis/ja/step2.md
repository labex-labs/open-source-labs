# 極座標軸を定義する

このステップでは、極座標軸を定義してスケーリング係数を設定します。極座標軸を定義するには、`PolarAxes.PolarTransform()` を使用します。

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Define the polar axes
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
