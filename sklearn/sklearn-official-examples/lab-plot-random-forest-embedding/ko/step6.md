# 비교를 위한 ExtraTreesClassifier 학습

이 단계에서는 비교를 위해 ExtraTreesClassifier 를 학습합니다.

```python
trees = ExtraTreesClassifier(max_depth=3, n_estimators=10, random_state=0)
trees.fit(X, y)
```
