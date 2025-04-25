# 计算指标

我们可以计算系数、均方误差和决定系数。

```python
from sklearn.metrics import mean_squared_error, r2_score

# 系数
print("系数：\n", regr.coef_)

# 均方误差
print("均方误差：%.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# 决定系数：1 表示完美预测
print("决定系数：%.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```
