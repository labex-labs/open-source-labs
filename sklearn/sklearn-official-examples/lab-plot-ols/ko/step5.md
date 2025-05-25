# 지표 계산

계수, 평균 제곱 오차, 결정 계수를 계산할 수 있습니다.

```python
from sklearn.metrics import mean_squared_error, r2_score

# 계수
print("계수: \n", regr.coef_)

# 평균 제곱 오차
print("평균 제곱 오차: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# 결정 계수: 1 은 완벽한 예측
print("결정 계수: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```
