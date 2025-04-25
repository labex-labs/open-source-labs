# 类型转换规则

当没有为所提供的输入类型实现核心循环时，会对通用函数的输入进行类型转换。转换规则决定了一种数据类型何时可以安全地转换为另一种数据类型。让我们看一个例子。

```python
import numpy as np

# 检查 int 是否可以安全地转换为 float
result = np.can_cast(np.int, np.float)

# 打印结果
print(result)
```

输出：

```
True
```
