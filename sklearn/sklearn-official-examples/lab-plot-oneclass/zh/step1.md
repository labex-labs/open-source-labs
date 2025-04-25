# 导入必要的库并生成数据

第一步是导入必要的库并生成数据。我们将使用 numpy 和 matplotlib 来生成和可视化数据，使用 scikit-learn 来构建单类支持向量机模型。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 生成训练数据
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# 生成一些常规的新观测值
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# 生成一些异常的新观测值
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
