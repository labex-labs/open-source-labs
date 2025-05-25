# 라이브러리 임포트

먼저, 사용자 정의 투영법을 생성하는 데 필요한 라이브러리를 임포트합니다.

```python
import numpy as np
import matplotlib
from matplotlib.axes import Axes
import matplotlib.axis as maxis
from matplotlib.patches import Circle
from matplotlib.path import Path
from matplotlib.projections import register_projection
import matplotlib.spines as mspines
from matplotlib.ticker import FixedLocator, Formatter, NullLocator
from matplotlib.transforms import Affine2D, BboxTransformTo, Transform
```
