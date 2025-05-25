# Treinar um ExtraTreesClassifier para Comparação

Neste passo, treinaremos um classificador ExtraTreesClassifier para comparação.

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
