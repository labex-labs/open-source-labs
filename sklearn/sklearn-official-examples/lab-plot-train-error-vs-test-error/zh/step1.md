# 生成样本数据

我们将使用 Scikit-learn 中的`make_regression()`函数来生成样本数据。我们将训练样本数量设置为 75，测试样本数量设置为 150，特征数量设置为 500。我们还将`n_informative`设置为 50，并将`shuffle`设置为 False。

```python
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_samples_train, n_samples_test, n_features = 75, 150, 500
X, y, coef = make_regression(
    n_samples=n_samples_train + n_samples_test,
    n_features=n_features,
    n_informative=50,
    shuffle=False,
    noise=1.0,
    coef=True,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_samples_train, test_size=n_samples_test, shuffle=False
)
```
