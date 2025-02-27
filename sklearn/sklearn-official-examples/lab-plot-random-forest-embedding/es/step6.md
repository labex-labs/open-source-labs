# Aprender un ExtraTreesClassifier para comparación

En este paso, aprenderemos un ExtraTreesClassifier para comparación.

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
