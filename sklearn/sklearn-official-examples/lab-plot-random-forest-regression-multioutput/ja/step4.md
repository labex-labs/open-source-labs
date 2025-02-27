# ランダムフォレスト回帰器を作成する

scikit-learnの`RandomForestRegressor`を使って、最大深さ30と推定器100個のランダムフォレスト回帰器を作成します。

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
