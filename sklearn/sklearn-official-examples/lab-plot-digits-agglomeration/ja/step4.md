# 特徴クラスタリングを実行する

このステップでは、scikit-learnの`FeatureAgglomeration`クラスを使って特徴クラスタリングを実行します。クラスタ数を32に設定します。

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
