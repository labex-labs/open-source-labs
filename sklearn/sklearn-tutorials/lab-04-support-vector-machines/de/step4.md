# Ungleiche Verteilungen

- SVMs können ungleiche Verteilungen durch Anpassen des Parameters `class_weight` behandeln:

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
