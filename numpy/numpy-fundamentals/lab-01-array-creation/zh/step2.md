# 使用 NumPy 内部数组创建函数

NumPy 提供了用于创建数组的内置函数。以下是一些示例：

```python
import numpy as np

# 创建一个值按规律递增的一维数组
arr1D = np.arange(10)

# 创建一个具有特定数据类型的一维数组
arr1D_float = np.arange(2, 10, dtype=float)

# 创建一个具有指定元素数量的一维数组
arr1D_linspace = np.linspace(1., 4., 6)

# 创建一个二维单位矩阵
identity_matrix = np.eye(3)

# 创建一个沿对角线具有给定值的二维数组
diag_matrix = np.diag([1, 2, 3])

# 创建一个范德蒙德矩阵
vander_matrix = np.vander([1, 2, 3, 4], 2)

# 创建一个全零数组
zeros_array = np.zeros((2, 3))

# 创建一个全一数组
ones_array = np.ones((2, 3))

# 创建一个填充随机值的数组
random_array = np.random.default_rng(42).random((2, 3))
```
