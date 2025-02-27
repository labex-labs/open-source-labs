# 多次元出力回帰器を作成する

基本的な推定器としてランダムフォレスト回帰器を使用して、`MultiOutputRegressor`を作成します。ステップ4と同じパラメータを使用します。

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
