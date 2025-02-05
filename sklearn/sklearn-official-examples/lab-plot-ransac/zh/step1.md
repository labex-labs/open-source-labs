# 导入库并生成数据

我们将导入必要的库，使用 make_regression 数据集生成随机数据，并向数据中添加异常值。

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

# 生成数据
n_samples = 1000
n_outliers = 50

X, y, coef = datasets.make_regression(
    n_samples=n_samples,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0,
)

# 添加异常值数据
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
```
