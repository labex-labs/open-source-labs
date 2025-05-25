# 추정기 적합

두 번째 단계는 다중 출력 추정기를 학습 데이터에 맞추는 것입니다. 우리는 극단적으로 무작위 트리, k-최근접 이웃, 선형 회귀 및 릿지 회귀의 네 가지 다른 알고리즘을 사용할 것입니다. 추정기는 얼굴의 상반부를 기반으로 얼굴의 하반부를 예측할 것입니다.

```python
# 추정기 적합
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```
