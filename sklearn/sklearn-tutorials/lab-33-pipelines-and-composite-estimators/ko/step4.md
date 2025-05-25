# 변환된 대상 회귀 분석기 (TransformedTargetRegressor)

`TransformedTargetRegressor` 클래스는 회귀 모델을 맞추기 전에 회귀 문제에서 대상 변수를 변환하는 데 사용됩니다. 대상 변수에 로그를 취하는 것과 같이 대상 변수에 변환을 적용하려는 경우 유용합니다. 예측은 역변환을 통해 원래 공간으로 매핑됩니다. 선형 회귀 모델과 사분위수 변환기를 사용하여 `TransformedTargetRegressor`를 사용하는 예는 다음과 같습니다.

```python
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.compose import TransformedTargetRegressor
from sklearn.preprocessing import QuantileTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)
transformer = QuantileTransformer(output_distribution='normal')
regressor = LinearRegression()
regr = TransformedTargetRegressor(regressor=regressor, transformer=transformer)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
regr.fit(X_train, y_train)
regr.score(X_test, y_test)
```
