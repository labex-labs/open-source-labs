# エイムズ住宅データの元のターゲットに対して線形回帰モデルを学習して評価する

エイムズ住宅データの元のターゲットに対して線形回帰モデルを学習して評価します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\n元のターゲットに対する線形回帰:")
for key, val in score.items():
    print(f"{key}: {val}")
```
