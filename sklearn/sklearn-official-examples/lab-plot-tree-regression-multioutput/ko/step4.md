# 예측

이 단계에서는 이전 단계에서 생성한 모델을 사용하여 예측을 수행합니다. `np.arange`를 사용하여 -100 부터 100 까지 0.01 간격의 새로운 값 배열을 생성한 다음, 모델의 `predict` 메서드를 사용하여 출력을 예측합니다.

```python
# 예측
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```
