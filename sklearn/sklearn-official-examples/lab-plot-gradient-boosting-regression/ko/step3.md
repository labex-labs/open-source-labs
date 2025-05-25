# 회귀 모델 학습

이제 그래디언트 부스팅 회귀 모델을 초기화하고 훈련 데이터로 학습시킵니다. 또한 테스트 데이터의 평균 제곱 오차를 확인해 보겠습니다.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("테스트 데이터의 평균 제곱 오차 (MSE): {:.4f}".format(mse))
```
