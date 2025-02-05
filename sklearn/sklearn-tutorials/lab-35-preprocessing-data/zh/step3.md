# 归一化

归一化是将单个样本缩放到具有单位范数的过程。当数据的大小不重要，而我们只对数据的方向（或角度）感兴趣时，通常会使用它。我们可以使用scikit-learn中的`Normalizer`来执行归一化。

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# 创建一个示例数据集
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# 初始化Normalizer
normalizer = Normalizer()

# 拟合并转换训练数据
X_normalized = normalizer.fit_transform(X)

# 打印转换后的数据
print(X_normalized)
```
