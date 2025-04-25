# エイムズ住宅データの変換後のターゲットに対して線形回帰モデルを学習して評価する

エイムズ住宅データに対して、変換後のターゲットを使って線形回帰モデルを学習して評価します。ここでは、TransformedTargetRegressor を使います。

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

print("\n変換後のターゲットに対する線形回帰：")
for key, val in score.items():
    print(f"{key}: {val}")
```
