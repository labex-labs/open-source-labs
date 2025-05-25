# 극좌표 축 정의

이 단계에서는 극좌표 축을 정의하고 스케일링 팩터를 설정합니다. `PolarAxes.PolarTransform()`을 사용하여 극좌표 축을 정의합니다.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Define the polar axes
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
