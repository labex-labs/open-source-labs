# 拟合非负最小二乘回归

现在我们将使用非负最小二乘回归来拟合数据。这可以通过在 scikit-learn 的 `LinearRegression` 类中设置 `positive=True` 参数来实现。然后，我们将预测测试集的值并计算 R2 分数。

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
