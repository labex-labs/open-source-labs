# ランダムフォレスト回帰器を作成する

scikit-learn の`RandomForestRegressor`を使って、最大深さ 30 と推定器 100 個のランダムフォレスト回帰器を作成します。

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
