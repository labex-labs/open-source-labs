# 逐次半分ランダム探索オブジェクトの作成

パラメータ空間を探索するための`HalvingRandomSearchCV`オブジェクトを作成します。このオブジェクトには以下の引数が必要です：

- `estimator`：最適化する推定器
- `param_distributions`：探索するパラメータ空間
- `factor`：各反復で候補の数を減らす割合
- `random_state`：探索に使用する乱数シード

オブジェクトを作成するコードは以下の通りです：

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
