# 필요한 라이브러리 및 데이터 가져오기

먼저 그리드를 생성하기 위해 필요한 라이브러리와 데이터를 가져와야 합니다. 플로팅을 위해 `matplotlib.pyplot`을 사용하고, 샘플 데이터 세트를 얻기 위해 `cbook`을 사용하며, 그리드를 생성하기 위해 `ImageGrid`를 사용합니다.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Get sample data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
```
