# 生成瑞士卷数据集

我们首先使用 `sklearn.datasets` 中的 `make_swiss_roll()` 函数生成瑞士卷数据集。此函数生成一个呈螺旋形状的三维数据集。

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```
