# 导入库并创建图形

第一步是导入必要的库并创建一个图形。我们使用 `matplotlib.pyplot` 模块来创建图形，并使用 `mpl_toolkits.axes_grid1` 模块为 y 轴标签留出空间。

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```
