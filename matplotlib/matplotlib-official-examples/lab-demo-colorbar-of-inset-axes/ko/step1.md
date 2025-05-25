# 라이브러리 및 데이터 가져오기

먼저, 플롯에 사용될 필요한 라이브러리와 데이터를 가져옵니다.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes

fig, ax = plt.subplots(figsize=[5, 4])

Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
```
