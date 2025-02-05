# 定义极坐标轴

在这一步中，我们将定义极坐标轴并设置缩放因子。我们将使用 `PolarAxes.PolarTransform()` 来定义极坐标轴。

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# 定义极坐标轴
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
