# 缩放

将特征缩放到特定范围是另一种常见的预处理技术。当特征具有不同的尺度，而我们希望将它们都带到相似的范围时，这种技术很有用。`MinMaxScaler`和`MaxAbsScaler`可用于执行缩放。

```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
import numpy as np

# 创建一个示例数据集
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# 初始化MinMaxScaler
min_max_scaler = MinMaxScaler()

# 拟合并转换训练数据
X_minmax = min_max_scaler.fit_transform(X)

# 打印转换后的数据
print(X_minmax)

# 初始化MaxAbsScaler
max_abs_scaler = MaxAbsScaler()

# 拟合并转换训练数据
X_maxabs = max_abs_scaler.fit_transform(X)

# 打印转换后的数据
print(X_maxabs)
```
