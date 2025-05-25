# 레이더 차트 함수 정의

다음으로, 레이더 차트를 생성하는 함수를 정의합니다. 이 함수는 `num_vars`와 `frame`의 두 가지 인수를 받습니다. `num_vars`는 레이더 차트의 변수 수를 나타내고, `frame`은 축을 둘러싼 프레임의 모양을 지정합니다.

```python
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # code for the function goes here
```
