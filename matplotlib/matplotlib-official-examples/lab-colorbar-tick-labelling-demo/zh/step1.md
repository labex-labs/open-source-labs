# 导入必要的库并设置随机种子

首先，我们需要导入必要的库，并设置随机种子以确保可重复性。我们将使用 `numpy` 生成一些随机数据，使用 `matplotlib.pyplot` 创建可视化效果，并使用 `matplotlib` 中的 `cm` 定义颜色映射。

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
