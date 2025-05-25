# 필요한 모듈 가져오기

첫 번째 단계는 플롯에 필요한 모듈을 가져오는 것입니다. x 및 y 데이터를 생성하기 위해 `numpy`를 사용하고, 플롯을 생성하기 위해 `matplotlib.pyplot`을 사용하며, 두 번째 y 축을 생성하기 위해 `mpl_toolkits.axes_grid1`을 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
```
