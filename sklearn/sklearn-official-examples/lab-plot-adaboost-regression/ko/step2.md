# 의사결정 트리 및 AdaBoost 회귀자를 이용한 학습 및 예측

이제 분류기를 정의하고 데이터에 맞춥니다. 첫 번째 회귀자는 `max_depth=4`인 `DecisionTreeRegressor`로 정의합니다. 두 번째 회귀자는 `max_depth=4`인 `DecisionTreeRegressor`를 기본 학습자로 사용하는 `AdaBoostRegressor`로 정의합니다. 이 AdaBoost 회귀자는 `n_estimators=300`개의 기본 학습자로 구성합니다. 그런 다음 두 회귀자 모두를 데이터에 맞추고 동일한 데이터에 대한 예측을 수행하여 데이터에 얼마나 잘 맞는지 확인합니다.

```python
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

regr_1 = DecisionTreeRegressor(max_depth=4)

regr_2 = AdaBoostRegressor(
    DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng
)

regr_1.fit(X, y)
regr_2.fit(X, y)

y_1 = regr_1.predict(X)
y_2 = regr_2.predict(X)
```
