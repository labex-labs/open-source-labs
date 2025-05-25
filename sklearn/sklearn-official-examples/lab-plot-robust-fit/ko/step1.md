# 필요한 라이브러리 가져오기 및 데이터 생성

먼저 필요한 라이브러리를 가져오고 적합을 위한 데이터를 생성해야 합니다. 약간의 노이즈가 있는 사인 함수를 생성하고 X 와 y 모두에 오류를 도입하여 데이터를 손상시킬 것입니다.

```python
from matplotlib import pyplot as plt
import numpy as np

from sklearn.linear_model import (
    LinearRegression,
    TheilSenRegressor,
    RANSACRegressor,
    HuberRegressor,
)
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

np.random.seed(42)

X = np.random.normal(size=400)
y = np.sin(X)
# X 가 2 차원이 되도록 합니다.
X = X[:, np.newaxis]

X_test = np.random.normal(size=200)
y_test = np.sin(X_test)
X_test = X_test[:, np.newaxis]

y_errors = y.copy()
y_errors[::3] = 3

X_errors = X.copy()
X_errors[::3] = 3

y_errors_large = y.copy()
y_errors_large[::3] = 10

X_errors_large = X.copy()
X_errors_large[::3] = 10
```
