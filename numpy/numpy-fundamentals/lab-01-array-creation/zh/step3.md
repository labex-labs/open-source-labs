# 复制、连接或修改现有数组

创建数组后，你可以对其进行复制、连接或修改以创建新数组。将数组或其元素赋给新变量时，使用 `np.copy` 函数创建新数组，而不是创建原始数组的视图。以下是一个示例：

```python
import numpy as np

# 创建一个数组
a = np.array([1, 2, 3, 4])

# 创建该数组前两个元素的视图
b = a[:2]

# 修改视图
b += 1

# 打印原始数组和修改后的视图
print('a =', a, '; b =', b)
```

要连接数组，可以使用 `np.vstack`、`np.hstack` 和 `np.block` 等函数。以下是使用 `np.block` 将四个 2x2 数组连接成一个 4x4 数组的示例：

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```
