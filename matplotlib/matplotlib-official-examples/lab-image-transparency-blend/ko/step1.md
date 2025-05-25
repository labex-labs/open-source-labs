# 데이터 생성

2D 그리드에서 두 개의 2D 블롭 (blob) 을 생성하는 것으로 시작합니다. 하나의 블롭은 양수이고 다른 하나는 음수입니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

def normal_pdf(x, mean, var):
    return np.exp(-(x - mean)**2 / (2*var))

# 블롭이 존재할 공간을 생성합니다.
xmin, xmax, ymin, ymax = (0, 100, 0, 100)
n_bins = 100
xx = np.linspace(xmin, xmax, n_bins)
yy = np.linspace(ymin, ymax, n_bins)

# 블롭을 생성합니다. 값의 범위는 대략 -.0002 에서 .0002 입니다.
means_high = [20, 50]
means_low = [50, 60]
var = [150, 200]

gauss_x_high = normal_pdf(xx, means_high[0], var[0])
gauss_y_high = normal_pdf(yy, means_high[1], var[0])

gauss_x_low = normal_pdf(xx, means_low[0], var[1])
gauss_y_low = normal_pdf(yy, means_low[1], var[1])

weights = (np.outer(gauss_y_high, gauss_x_high)
           - np.outer(gauss_y_low, gauss_x_low))

# 픽셀이 페이드될 회색 배경도 생성합니다.
greys = np.full((*weights.shape, 3), 70, dtype=np.uint8)
```
