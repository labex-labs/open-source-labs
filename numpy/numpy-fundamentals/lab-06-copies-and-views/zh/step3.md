# 创建副本

可以通过复制数组的数据缓冲区和元数据来创建副本。要创建副本，可以使用 `ndarray` 对象的 `copy()` 方法。

```python
import numpy as np

# 创建一个数组
x = np.array([1, 2, 3, 4, 5])

# 创建一个副本
y = x.copy()

# 修改副本
y[0] = 10

# 打印原始数组
print(x)  # 输出：[1, 2, 3, 4, 5]
```

在上述示例中，副本 `y` 与原始数组 `x` 相互独立。
