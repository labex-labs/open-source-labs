# 라이브러리 가져오기 및 Figure 생성

첫 번째 단계는 필요한 라이브러리를 가져와 Figure 를 생성하는 것입니다. `matplotlib.pyplot` 모듈을 사용하여 Figure 를 생성하고, `mpl_toolkits.axes_grid1` 모듈을 사용하여 y-label 을 위한 공간을 만듭니다.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```
