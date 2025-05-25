# 가장 불확실한 포인트에 레이블 추가

사용자로부터 레이블을 받아 레이블이 지정된 데이터 포인트에 추가하고, 이를 사용하여 모델을 다시 학습합니다.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```
