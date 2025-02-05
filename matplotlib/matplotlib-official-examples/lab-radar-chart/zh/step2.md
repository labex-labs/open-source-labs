# 定义雷达图函数

接下来，我们将定义一个创建雷达图的函数。这个函数将接受两个参数：`num_vars` 和 `frame`。`num_vars` 是雷达图的变量数量，`frame` 指定围绕坐标轴的框架形状。

```python
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # 函数的代码写在这里
```
