# 比較用にExtraTreesClassifierを学習する

このステップでは、比較用にExtraTreesClassifierを学習します。

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
