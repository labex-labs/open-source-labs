# 重写通用函数行为

包括 ndarray 子类在内的类，可以通过定义某些特殊方法来重写通用函数对它们的作用方式。这允许对通用函数的行为进行定制。让我们看一个例子。

```python
import numpy as np

# 定义一个自定义类
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Custom add method called")
        return super().__add__(other)

# 创建自定义类的一个实例
arr = MyArray([1, 2, 3])

# 执行加法
result = arr + 1

# 打印结果
print(result)
```

输出：

```
Custom add method called
[2 3 4]
```
