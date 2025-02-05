# 缺失值插补

数据集中的缺失值可能会给机器学习算法带来问题。我们可以使用scikit-learn的`impute`模块中提供的方法来处理缺失值。在这里，我们将使用`SimpleImputer`来插补缺失值。

```python
from sklearn.impute import SimpleImputer
import numpy as np

# 创建一个带有缺失值的示例数据集
X = np.array([[1., 2., np.nan],
              [3., np.nan, 5.],
              [np.nan, 4., 6.]])

# 初始化SimpleImputer
imputer = SimpleImputer()

# 拟合并转换训练数据
X_imputed = imputer.fit_transform(X)

# 打印转换后的数据
print(X_imputed)
```
