# 필요한 라이브러리 가져오기 및 난수 상태 고정

먼저, 필요한 라이브러리를 가져오고 재현성을 위해 난수 상태를 고정해야 합니다. `numpy`를 사용하여 일부 임의 데이터를 생성하고, 시각화를 위해 `matplotlib.pyplot`을 사용하며, 컬러 맵을 정의하기 위해 `matplotlib`에서 `cm`을 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
