# 导入必要的库并加载合成数据

我们首先导入必要的库并加载合成数据。我们生成一个合成随机回归数据集，并通过平移所有目标值来修改目标，使所有条目均为非负，然后应用指数函数以获得无法使用简单线性模型拟合的非线性目标。然后，我们在训练线性回归模型并将其用于预测之前，使用对数函数（np.log1p）和指数函数（np.expm1）来转换目标。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Generate synthetic data
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modify the targets
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
