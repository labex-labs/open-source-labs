# 선형 회귀 모델 학습

다음으로, 학습 데이터셋에 선형 회귀 모델을 적합합니다.

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```
