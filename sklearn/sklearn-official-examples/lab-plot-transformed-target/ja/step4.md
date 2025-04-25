# 変換後のターゲットに対して線形回帰モデルを学習して評価する

TransformedTargetRegressor を使って、変換後のターゲットに対して線形回帰モデルを学習して評価します。対数関数はターゲットを線形化し、中央絶対誤差（MedAE）によって報告されるように、同様の線形モデルでもより良い予測が可能になります。

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
