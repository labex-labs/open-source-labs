# 特徴クラスタリングを実行する

このステップでは、scikit-learn の`FeatureAgglomeration`クラスを使って特徴クラスタリングを実行します。クラスタ数を 32 に設定します。

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
