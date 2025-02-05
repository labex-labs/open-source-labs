# 基本算术运算

基本的通用函数对标量进行操作，最简单的例子就是加法运算符。让我们看看如何使用加法运算符按元素对两个数组进行相加。

```python
import numpy as np

# 创建两个数组
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# 按元素相加数组
result = arr1 + arr2

# 打印结果
print(result)
```

输出：

```
array([1, 3, 2, 6])
```
