# レーダーチャート関数の定義

次に、レーダーチャートを作成する関数を定義します。この関数は2つの引数を取ります。`num_vars`と`frame`です。`num_vars`はレーダーチャートの変数の数であり、`frame`は軸を囲む枠の形状を指定します。

```python
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # 関数のコードはここに記載します
```
