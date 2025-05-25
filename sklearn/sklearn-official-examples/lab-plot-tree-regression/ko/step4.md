# 예측

0 부터 5 까지의 범위에서 모델을 사용하여 예측을 수행합니다.

```python
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
```
