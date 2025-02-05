# 生成样本数据

在这一步中，我们使用一个高度非高斯过程（自由度较低的双学生t分布）来生成样本数据。

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# 混合数据
A = np.array([[1, 1], [0, 2]])  # 混合矩阵

X = np.dot(S, A.T)  # 生成观测值
```
