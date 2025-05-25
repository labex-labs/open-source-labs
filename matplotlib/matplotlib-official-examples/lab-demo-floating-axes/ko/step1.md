# 필요한 라이브러리 가져오기

먼저, 필요한 라이브러리를 가져와야 합니다. Matplotlib, NumPy, 그리고 `mpl_toolkits.axisartist` 및 `mpl_toolkits.axisartist.grid_finder`의 일부 모듈을 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.angle_helper as angle_helper
import mpl_toolkits.axisartist.floating_axes as floating_axes
from mpl_toolkits.axisartist.grid_finder import (DictFormatter, FixedLocator,
                                                 MaxNLocator)
```
