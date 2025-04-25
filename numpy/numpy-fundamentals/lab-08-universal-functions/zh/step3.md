# 输出类型确定

如果并非所有输入参数都是 ndarray，通用函数的输出不一定是 ndarray。输出类型可以根据输入类型和类型转换规则来确定。让我们看一个例子。

```python
import numpy as np

# 创建一个数组
arr = np.arange(9).reshape(3, 3)

# 执行乘法并指定输出类型
result = np.multiply.reduce(arr, dtype=float)

# 打印结果
print(result)
```

输出：

```
array([ 0., 28., 80.])
```
