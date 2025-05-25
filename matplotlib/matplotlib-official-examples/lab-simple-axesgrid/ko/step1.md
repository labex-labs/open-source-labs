# 필요한 라이브러리 가져오기 및 이미지 배열 생성

필요한 라이브러리를 가져오고 NumPy 라이브러리의 `arange` 및 `reshape` 함수를 사용하여 10x10 이미지 배열 4 개를 생성하는 것으로 시작합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
