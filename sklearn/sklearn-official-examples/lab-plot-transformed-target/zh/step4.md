# 在转换后的目标上训练并评估线性回归模型

我们使用 TransformedTargetRegressor 在转换后的目标上训练并评估一个线性回归模型。对数函数使目标线性化，即使使用与中位数绝对误差（MedAE）报告的类似线性模型，也能实现更好的预测。

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\nLinear Regression on transformed targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```
