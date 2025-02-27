# Dichteschätzung und Neuentdeckungsdetection

- SVMs können auch zur Dichteschätzung und Neuentdeckungsdetection mit der Klasse `OneClassSVM` verwendet werden:

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
