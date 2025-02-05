# 判断数组是视图还是副本

你可以使用 `ndarray` 对象的 `base` 属性来判断一个数组是视图还是副本。对于视图，`base` 属性返回原始数组；对于副本，`base` 属性返回 `None`。例如：

```python
import numpy as np

# 创建一个数组
x = np.arange(9)

# 创建一个视图
y = x.reshape(3, 3)

# 创建一个副本
z = y[[2, 1]]

# 检查 y 是否是视图
print(y.base)  # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 检查 z 是否是副本
print(z.base is None)  # 输出: True
```

在上述示例中，`y` 是视图，`z` 是副本。
