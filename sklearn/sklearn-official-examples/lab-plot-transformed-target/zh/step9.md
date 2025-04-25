# 针对艾姆斯房屋数据的变换后目标训练并评估线性回归模型

我们使用变换后目标，通过变换目标回归器（TransformedTargetRegressor）针对艾姆斯房屋数据训练并评估一个线性回归模型。

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(),
    transformer=QuantileTransformer(n_quantiles=900, output_distribution="normal"),
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\n针对变换后目标的线性回归：")
for key, val in score.items():
    print(f"{key}: {val}")
```
