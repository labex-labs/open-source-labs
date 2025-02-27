# Обучение классификатора ExtraTreesClassifier для сравнения

В этом шаге мы обучим классификатор ExtraTreesClassifier для сравнения.

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
