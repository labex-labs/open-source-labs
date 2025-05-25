# SGD 를 사용한 회귀자 학습

다음으로, SGDRegressor 클래스를 사용하여 회귀자를 학습할 것입니다. squared_error 손실 함수와 l2 페널티를 사용할 것입니다.

```python
# SGD 를 사용한 회귀자 학습
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# 테스트 세트에서 예측 수행
y_pred = reg.predict(X_test)

# 회귀자의 평균 제곱 오차 측정
mse = mean_squared_error(y_test, y_pred)

# 평균 제곱 오차 출력
print("회귀자 평균 제곱 오차:", mse)
```
