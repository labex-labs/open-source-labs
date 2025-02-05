# 数据生成

我们通过对 `numpy.random.randn` 返回的标准正态分布进行随机采样，生成两个组件（每个组件包含 `n_samples` 个样本）。一个组件保持球形，但进行了平移和重新缩放。另一个组件则变形为具有更一般的协方差矩阵。

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # 一般
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # 球形

X = np.concatenate([component_1, component_2])
```
