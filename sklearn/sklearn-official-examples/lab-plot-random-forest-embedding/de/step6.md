# Lernen eines ExtraTreesClassifier zum Vergleich

In diesem Schritt werden wir einen ExtraTreesClassifier lernen, um einen Vergleich durchzuführen.

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
