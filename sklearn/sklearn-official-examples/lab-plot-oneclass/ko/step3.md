# 오류 개수 계산

모델이 학습 데이터, 일반적인 새로운 관측치 및 비정상적인 새로운 관측치에서 발생시킨 오류 개수를 계산합니다.

```python
# 오류 개수 계산
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
