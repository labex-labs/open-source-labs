# 准备数据

我们首先准备具有正弦关系和一些高斯噪声的虚拟数据。我们使用 NumPy 的 `linspace()` 函数创建一个在 0 到 6 之间均匀分布的 100 个值的一维数组。然后，我们使用 `np.newaxis` 属性将一维数组转换为形状为 `(100,1)` 的二维数组。我们对这个数组应用 `sin()` 函数，并添加通过将数组乘以 6 得到的第二个正弦波。然后，我们使用 NumPy 的 `normal()` 函数添加一些均值为 0、标准差为 0.1 的高斯噪声。

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
