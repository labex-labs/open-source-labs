# Apprendre un ExtraTreesClassifier pour la comparaison

Dans cette étape, nous allons apprendre un ExtraTreesClassifier pour la comparaison.

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
