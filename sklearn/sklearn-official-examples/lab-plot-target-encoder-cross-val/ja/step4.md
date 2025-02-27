# 生データで Ridge 回帰モデルを学習させる

このセクションでは、エンコーディングを行ったデータセットと行っていないデータセットで Ridge 回帰モデルを学習させ、区間交差検証（interval cross-validation）の有無によるターゲットエンコーダの影響を調べます。まず、生の特徴量で Ridge モデルを学習させます。以下のコードを実行して、Ridge モデルを学習させてください。

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
