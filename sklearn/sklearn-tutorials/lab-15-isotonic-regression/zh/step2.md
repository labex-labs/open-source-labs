# 创建示例数据

接下来，我们需要创建一些示例数据来拟合我们的保序回归模型。在这个例子中，我们将生成两个数组 `X` 和 `y`，分别代表输入数据和目标值。

```python
import numpy as np

# 生成随机输入数据
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```
