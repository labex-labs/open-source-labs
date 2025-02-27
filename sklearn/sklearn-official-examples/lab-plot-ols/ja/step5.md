# 評価指標を計算する

係数、平均二乗誤差、決定係数を計算することができます。

```python
from sklearn.metrics import mean_squared_error, r2_score

# 係数
print("Coefficients: \n", regr.coef_)

# 平均二乗誤差
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# 決定係数: 1は完全な予測
print("Coefficient of determination: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```
