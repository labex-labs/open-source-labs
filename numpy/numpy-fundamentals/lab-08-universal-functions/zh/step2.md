# 通用函数方法

通用函数有四种方法：reduce、accumulate、reduceat 和 outer。这些方法对于在数组上执行操作很有用。让我们看看 reduce 方法。

```python
import numpy as np

# 创建一个数组
arr = np.arange(9).reshape(3, 3)

# 沿第一个轴对数组进行规约
result = np.add.reduce(arr, 1)

# 打印结果
print(result)
```

输出：

```
array([ 3, 12, 21])
```
