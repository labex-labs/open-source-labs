# 모델 평가

학습된 모델을 테스트 데이터와 이상치 데이터로 평가합니다. `predict` 메서드를 사용하여 테스트 데이터와 이상치 데이터의 레이블을 예측합니다. 그런 다음 테스트 데이터와 이상치 데이터에서 오류 수를 계산합니다.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
