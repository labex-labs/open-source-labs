# 标准化

标准化是许多机器学习算法常见的预处理步骤。它将特征转换为均值为零、方差为一。我们可以使用scikit-learn中的`StandardScaler`来执行标准化。

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# 创建一个示例数据集
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# 初始化StandardScaler
scaler = StandardScaler()

# 在训练数据上拟合scaler
scaler.fit(X)

# 转换训练数据
X_scaled = scaler.transform(X)

# 打印转换后的数据
print(X_scaled)
```
