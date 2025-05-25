# 샘플 데이터 생성

Scikit-learn 의 `make_regression()` 함수를 사용하여 샘플 데이터를 생성합니다. 학습 샘플 수는 75 개, 테스트 샘플 수는 150 개, 특징 (feature) 수는 500 개로 설정합니다. 또한 `n_informative`를 50 으로, `shuffle`를 False 로 설정합니다.

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
