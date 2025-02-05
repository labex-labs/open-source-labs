# 导入必要的库和数据

我们首先需要导入必要的库和数据来创建我们的网格。我们将使用 `matplotlib.pyplot` 进行绘图，使用 `cbook` 获取示例数据集，并使用 `ImageGrid` 创建我们的网格。

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# 获取示例数据
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 数组
extent = (-3, 4, -4, 3)
```
