# 比較用に ExtraTreesClassifier を学習する

このステップでは、比較用に ExtraTreesClassifier を学習します。

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
