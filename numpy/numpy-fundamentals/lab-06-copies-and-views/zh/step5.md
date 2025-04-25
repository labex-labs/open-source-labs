# 其他操作

在 NumPy 中还有其他一些操作也可能会创建视图或副本。

- `reshape()` 函数在可能的情况下创建视图，否则创建副本。例如：

```python
import numpy as np

# 创建一个数组
x = np.ones((2, 3))

# 转置数组
y = x.T

# 尝试重塑数组
try:
    y.shape = 6
except AttributeError:
    print("Incompatible shape for in-place modification. Use `.reshape()` to make a copy with the desired shape.")
```

在上述示例中，数组 `y` 在转置后变得不连续，因此重塑它需要进行复制。

- `ravel()` 函数在可能的情况下返回数组的连续扁平视图。另一方面，`flatten()` 方法总是返回数组的扁平副本。例如：

```python
import numpy as np

# 创建一个数组
x = np.arange(9).reshape(3, 3)

# 创建一个扁平视图
y = x.ravel()

# 创建一个扁平副本
z = x.flatten()

# 打印原始数组
print(x)  # 输出：[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

在上述示例中，`y` 是一个视图，而 `z` 是一个副本。
