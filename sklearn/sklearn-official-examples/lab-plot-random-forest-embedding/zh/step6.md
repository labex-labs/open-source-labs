# 学习一个ExtraTreesClassifier用于比较

在这一步中，我们将学习一个ExtraTreesClassifier用于比较。

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
