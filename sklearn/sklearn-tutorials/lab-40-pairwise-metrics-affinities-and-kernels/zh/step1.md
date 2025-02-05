# 距离度量

距离度量是衡量两个对象之间差异程度的函数。这些度量满足某些条件，例如非负性、对称性和三角不等式。

一些常见的距离度量包括欧几里得距离、曼哈顿距离和闵可夫斯基距离。

让我们使用 `pairwise_distances` 函数计算两组样本之间的成对距离：

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# 计算 X 和 Y 之间的成对距离
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

输出：

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
