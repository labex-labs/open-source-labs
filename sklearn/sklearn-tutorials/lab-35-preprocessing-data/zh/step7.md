# 创建自定义转换器

在某些情况下，我们可能希望将现有的 Python 函数转换为转换器，以协助进行数据清理或处理。我们可以使用 scikit-learn 中的`FunctionTransformer`来实现这一点。

```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

# 创建一个自定义函数
def custom_function(X):
    return np.log1p(X)

# 初始化 FunctionTransformer
transformer = FunctionTransformer(custom_function)

# 创建一个示例数据集
X = np.array([[0, 1],
              [2, 3]])

# 使用自定义函数转换数据
X_transformed = transformer.transform(X)

# 打印转换后的数据
print
```
