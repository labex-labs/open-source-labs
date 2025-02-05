# 拟合经典线性回归

现在我们将使用经典线性回归来拟合数据。这通过使用 scikit-learn 的 `LinearRegression` 类来完成。然后，我们将预测测试集的值并计算 R2 分数。

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
