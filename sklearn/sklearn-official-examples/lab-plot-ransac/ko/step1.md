# 라이브러리 가져오기 및 데이터 생성

필요한 라이브러리를 가져오고 `make_regression` 데이터셋을 사용하여 랜덤 데이터를 생성하고 데이터에 이상치를 추가합니다.

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

# 데이터 생성
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

# 이상치 데이터 추가
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
```
